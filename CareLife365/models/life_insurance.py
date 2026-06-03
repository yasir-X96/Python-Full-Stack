from .insurance_policy import InsurancePolicy

class LifeInsurance(InsurancePolicy):
    def __init__(self, policy_id, policy_name, premium_amount, policy_duration, coverage_amount, nominee_name, sum_assured):
        super().__init__(policy_id, policy_name, premium_amount, policy_duration, coverage_amount)
        self.nominee_name = nominee_name
        self.sum_assured = sum_assured

    def display_life_policy(self):
        return f"{self.display_policy_details()} | Nominee: {self.nominee_name}, Sum Assured: {self.sum_assured}"

    def calculate_premium(self):
        return self.premium_amount * 1.15

    def display_policy(self):
        return self.display_life_policy()
