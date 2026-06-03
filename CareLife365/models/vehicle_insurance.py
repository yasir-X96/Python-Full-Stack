from .insurance_policy import InsurancePolicy

class VehicleInsurance(InsurancePolicy):
    def __init__(self, policy_id, policy_name, premium_amount, policy_duration, coverage_amount, vehicle_number, vehicle_type, vehicle_value):
        super().__init__(policy_id, policy_name, premium_amount, policy_duration, coverage_amount)
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.vehicle_value = vehicle_value

    def display_vehicle_policy(self):
        return f"{self.display_policy_details()} | Vehicle: {self.vehicle_number}, Type: {self.vehicle_type}, Value: {self.vehicle_value}"

    def calculate_premium(self):
        return self.premium_amount * 1.20

    def display_policy(self):
        return self.display_vehicle_policy()
