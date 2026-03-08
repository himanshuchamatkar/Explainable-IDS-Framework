import json
import os
from datetime import datetime


class PredictionLogger:

    def __init__(self):
        self.file = "realtime_predictions.json"

    def log(self, src_ip, protocol, packets, prediction, probability, explanation):

        # Fix possible missing IP
        if not src_ip:
            src_ip = "unknown"

        entry = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "src_ip": src_ip,
            "protocol": protocol,              # NEW FIELD
            "flow_packets": packets,
            "prediction": prediction,
            "probability": probability,
            "explanation": explanation
        }

        # Load previous data
        if os.path.exists(self.file):
            try:
                with open(self.file, "r") as f:
                    data = json.load(f)
            except:
                data = []
        else:
            data = []

        data.append(entry)

        # Save updated log
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)