import json

class PolicyService:
    def save_policies(self, policies, filename="data/policies.json"):
        data = [vars(p) for p in policies]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_policies(self, filename="data/policies.json"):
        with open(filename, "r") as f:
            return json.load(f)
