class InsuranceClaim:
    def __init__(self, claim_id, claim_amount, claim_status, hospital_name):
        self.claim_id = claim_id
        self.claim_amount = claim_amount
        self.claim_status = claim_status
        self.hospital_name = hospital_name

    def __str__(self):
        return f"Claim[{self.claim_id}] {self.claim_status} | Amount: {self.claim_amount} | Hospital: {self.hospital_name}"
