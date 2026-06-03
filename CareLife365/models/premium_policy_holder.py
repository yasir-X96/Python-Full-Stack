from .policy_holder import PolicyHolder

class PremiumPolicyHolder(PolicyHolder):
    def __init__(self, policy_holder_id, name, age, mobile_number, city, loyalty_points, discount_percentage):
        super().__init__(policy_holder_id, name, age, mobile_number, city)
        self.loyalty_points = loyalty_points
        self.discount_percentage = discount_percentage

    def calculate_discount(self, premium_amount):
        return premium_amount - (premium_amount * self.discount_percentage / 100)

    def display_customer_profile(self):
        return (f"PolicyHolder {self.name} (Age: {self.age}) from {self.city}, "
                f"Loyalty Points: {self.loyalty_points}, Discount: {self.discount_percentage}%")

    def __str__(self):
        return f"PremiumPolicyHolder[{self.policy_holder_id}] {self.name}"
    