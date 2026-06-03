from .insurance_policy import InsurancePolicy

class HealthInsurance(InsurancePolicy):
    def __init__(self, policy_id, policy_name, premium_amount, policy_duration, coverage_amount, hospital_network, room_rent_limit):
        super().__init__(policy_id, policy_name, premium_amount, policy_duration, coverage_amount)
        self.hospital_network = hospital_network
        self.room_rent_limit = room_rent_limit

    def display_health_policy(self):
        return f"{self.display_policy_details()} | Hospital Network: {self.hospital_network}, Room Rent Limit: {self.room_rent_limit}"

    def calculate_premium(self):
        return self.premium_amount * 1.10

    def display_policy(self):
        return self.display_health_policy()
