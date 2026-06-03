class PolicyHolder:
    def __init__(self, policy_holder_id, name, age, mobile_number, city, active_policy_count=0):
        self.policy_holder_id = policy_holder_id
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.city = city
        self.active_policy_count = active_policy_count

    def display_policyholder(self):
        return f"{self.name} ({self.age}) from {self.city}, Active Policies: {self.active_policy_count}"

    def update_mobile_number(self, new_number):
        self.mobile_number = new_number

    def increase_active_policy_count(self):
        self.active_policy_count += 1

    def __str__(self):
        return f"PolicyHolder[{self.policy_holder_id}] {self.name}"
