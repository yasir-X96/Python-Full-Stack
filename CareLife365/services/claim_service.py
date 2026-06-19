import json

class ClaimService:
    def save_claims(self, claims, filename="data/claims.json"):
        data = [vars(c) for c in claims]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_claims(self, filename="data/claims.json"):
        with open(filename, "r") as f:
            return json.load(f)
