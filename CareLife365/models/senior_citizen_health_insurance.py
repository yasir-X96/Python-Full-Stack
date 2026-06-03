from .health_insurance import HealthInsurance

class SeniorCitizenHealthInsurance(HealthInsurance):
    def __init__(self, policy_id, policy_name, premium_amount, policy_duration, coverage_amount, hospital_network, room_rent_limit, age_limit, annual_health_checkup):
        super().__init__(policy_id, policy_name, premium_amount, policy_duration, coverage_amount, hospital_network, room_rent_limit)
        self.age_limit = age_limit
        self.annual_health_checkup = annual_health_checkup

    def display_senior_policy(self):
        return f"{super().display_health_policy()} | Age Limit: {self.age_limit}, Annual Checkup: {self.annual_health_checkup}"

    def calculate_premium(self):
        return self.premium_amount * 1.05

    def display_policy(self):
        return self.display_senior_policy()
