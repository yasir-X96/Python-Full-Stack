from abc import ABC, abstractmethod

class InsurancePolicy(ABC):
    def __init__(self, policy_id, policy_name, premium_amount, policy_duration, coverage_amount):
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.premium_amount = premium_amount
        self.policy_duration = policy_duration
        self.coverage_amount = coverage_amount

    def display_policy_details(self):
        return f"{self.policy_name} | Premium: {self.premium_amount} | Coverage: {self.coverage_amount}"

    def renew_policy(self, extra_years):
        self.policy_duration += extra_years

    def update_coverage_amount(self, new_amount):
        self.coverage_amount = new_amount

    @abstractmethod
    def calculate_premium(self):
        pass

    @abstractmethod
    def display_policy(self):
        pass

    def __str__(self):
        return f"InsurancePolicy[{self.policy_id}] {self.policy_name}"
