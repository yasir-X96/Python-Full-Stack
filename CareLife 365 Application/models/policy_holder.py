class PolicyHolder:

    def __init__(self,
                 policy_holder_id,
                 name,
                 age,
                 mobile_number,
                 city):

        self.policy_holder_id = policy_holder_id
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.city = city
        self.active_policy_count = 0

    def display_policyholder(self):

        print("\n------Policy Holder Details------")
        print("Policy Holder Id :", self.policy_holder_id)
        print("Name             :", self.name)
        print("Age              :", self.age)
        print("Mobile Number    :", self.mobile_number)
        print("City             :", self.city)
        print("Active Policies  :", self.active_policy_count)

    def update_mobile_number(self, mobile):

        self.mobile_number = mobile
        print("Mobile Number Updated Successfully")

    def increase_active_policy_count(self):

        self.active_policy_count += 1
        print("Policy Count Increased Successfully")

    def __str__(self):

        return (f"PolicyHolder(Id={self.policy_holder_id}, "
                f"Name={self.name}, "
                f"Age={self.age}, "
                f"City={self.city})")


class PremiumPolicyHolder(PolicyHolder):

    def __init__(self,
                 policy_holder_id,
                 name,
                 age,
                 mobile_number,
                 city,
                 loyalty_points,
                 discount_percentage):

        super().__init__(
            policy_holder_id,
            name,
            age,
            mobile_number,
            city
        )

        self.loyalty_points = loyalty_points
        self.discount_percentage = discount_percentage

    def calculate_discount(self, amount):

        discount = amount * self.discount_percentage / 100
        return discount

    def display_customer_profile(self):

        print("\n------Premium Customer Profile------")
        print("Policy Holder Id :", self.policy_holder_id)
        print("Name             :", self.name)
        print("Age              :", self.age)
        print("City             :", self.city)
        print("Loyalty Points   :", self.loyalty_points)
        print("Discount %       :", self.discount_percentage)

    def __str__(self):

        return (f"PremiumPolicyHolder("
                f"Name={self.name}, "
                f"Points={self.loyalty_points}, "
                f"Discount={self.discount_percentage}%)")