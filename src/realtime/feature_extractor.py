import numpy as np


class FeatureExtractor:

    def extract(self, flow_packets):

        packet_lengths = [p["length"] for p in flow_packets]
        timestamps = [p["timestamp"] for p in flow_packets]

        flow_duration = max(timestamps) - min(timestamps)

        total_packets = len(packet_lengths)
        total_bytes = sum(packet_lengths)

        packet_len_mean = np.mean(packet_lengths)
        packet_len_std = np.std(packet_lengths)

        packets_per_sec = 0
        bytes_per_sec = 0

        if flow_duration > 0:
            packets_per_sec = total_packets / flow_duration
            bytes_per_sec = total_bytes / flow_duration

        features = {
            "flow_duration": flow_duration,
            "total_packets": total_packets,
            "total_bytes": total_bytes,
            "packet_length_mean": packet_len_mean,
            "packet_length_std": packet_len_std,
            "packets_per_sec": packets_per_sec,
            "bytes_per_sec": bytes_per_sec
        }

        return features     