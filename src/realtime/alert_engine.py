import json
import os
from datetime import datetime

class AlertEngine:

    def __init__(self):
        self.file = "alerts.json"

    def trigger(self, src_ip, attack_type, probability):

        alert = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "src_ip": src_ip,
            "attack_type": attack_type,
            "probability": probability
        }

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                data = json.load(f)

        else:
            data = []

        data.append(alert)

        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)