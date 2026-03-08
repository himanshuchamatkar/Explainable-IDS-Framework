from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import time

from src.realtime.flow_builder import FlowBuilder
from src.realtime.feature_extractor import FeatureExtractor
from src.realtime.realtime_predictor import RealtimePredictor
from src.realtime.prediction_logger import PredictionLogger

# NEW IMPORTS
from src.realtime.alert_engine import AlertEngine
from src.realtime.threat_intelligence import threat_level


class PacketCapture:

    def __init__(self):

        self.packet_count = 0

        # Flow builder
        self.flow_builder = FlowBuilder()

        # Feature extractor
        self.feature_extractor = FeatureExtractor()

        # ML predictor
        self.predictor = RealtimePredictor()

        # Logger for dashboard
        self.logger = PredictionLogger()

        # NEW: Alert engine
        self.alert_engine = AlertEngine()

    def process_packet(self, packet):

        try:

            if IP not in packet:
                return

            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            packet_len = len(packet)

            src_port = 0
            dst_port = 0
            protocol = "OTHER"

            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                protocol = "TCP"

            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                protocol = "UDP"

            self.packet_count += 1
            print(f"Packet: {self.packet_count}")

            packet_info = {
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "src_port": src_port,
                "dst_port": dst_port,
                "protocol": protocol,
                "length": packet_len,
                "timestamp": time.time()
            }

            # Add packet to flow builder
            self.flow_builder.add_packet(packet_info)

            # Check completed flows
            completed_flows = self.flow_builder.flush_flows()

            if completed_flows:

                print("\n=== REALTIME IDS ===")

                for flow in completed_flows:

                    # Extract features
                    features = self.feature_extractor.extract(flow)

                    # Run ML prediction
                    result = self.predictor.predict(features)

                    flow_packets = result["flow_packets"]
                    label = result["prediction"]
                    probability = result["probability"]
                    explanation = result["explanation"]

                    # Get attacker IP
                    attacker_ip = flow[0].get("src_ip", "unknown")

                    # Calculate threat severity
                    severity = threat_level(probability)

                    print(f"\nSource IP: {attacker_ip}")
                    print(f"Flow packets: {flow_packets}")
                    print(f"Prediction: {label}")
                    print(f"Attack Probability: {round(probability,4)}")
                    print(f"Threat Level: {severity}")

                    # Trigger alert if high severity
                    if severity in ["HIGH", "CRITICAL"]:

                        self.alert_engine.trigger(
                            attacker_ip,
                            label,
                            probability
                        )

                    # Log prediction for dashboard
                    self.logger.log(
    attacker_ip,
    protocol,
    flow_packets,
    label,
    probability,
    explanation
)

                print("====================\n")

        except Exception as e:
            print("Packet processing error:", e)

    def start_capture(self):

        print("\nStarting realtime IDS...")
        print("Press CTRL + C to stop.\n")

        sniff(
            iface="Realtek RTL8852AE WiFi 6 802.11ax PCIe Adapter",
            prn=self.process_packet,
            store=False
        )