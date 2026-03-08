import time
from collections import defaultdict


class FlowBuilder:

    def __init__(self):

        self.flows = defaultdict(list)
        self.last_flush = time.time()

        # flush flows every 5 seconds
        self.flush_interval = 5

    def get_flow_id(self, src_ip, dst_ip, src_port, dst_port, protocol):

        return (src_ip, dst_ip, src_port, dst_port, protocol)

    def add_packet(self, packet_info):

        flow_id = self.get_flow_id(
            packet_info["src_ip"],
            packet_info["dst_ip"],
            packet_info["src_port"],
            packet_info["dst_port"],
            packet_info["protocol"]
        )

        self.flows[flow_id].append(packet_info)

    def flush_flows(self):

        current_time = time.time()

        if current_time - self.last_flush < self.flush_interval:
            return []

        completed = []

        for flow_id, packets in self.flows.items():
            completed.append(packets)

        self.flows.clear()

        self.last_flush = current_time

        return completed    