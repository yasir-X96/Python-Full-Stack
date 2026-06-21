from abc import ABC, abstractmethod


class InsurancePolicy(ABC):

    def __init__(self,
                 policy_id,
                 policy_name,
                 premium_amount,
                 policy_duration,
                 coverage_amount):

        self.policy_id = policy_id
        self.policy_name = policy_name
        self.premium_amount = premium_amount
        self.policy_duration = policy_duration
        self.coverage_amount = coverage_amount

    def renew_policy(self):

        self.policy_duration += 1
        print("Policy Renewed Successfully")

    def update_coverage_amount(self, amount):

        self.coverage_amount = amount
        print("Coverage Updated Successfully")

    @abstractmethod
    def calculate_premium(self):
        pass

    @abstractmethod
    def display_policy(self):
        pass

    def __str__(self):

        return (f"InsurancePolicy("
                f"Id={self.policy_id}, "
                f"Name={self.policy_name})")


class HealthInsurance(InsurancePolicy):

    def __init__(self,
                 policy_id,
                 policy_name,
                 premium_amount,
                 policy_duration,
                 coverage_amount,
                 hospital_network,
                 room_rent_limit):

        super().__init__(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount
        )

        self.hospital_network = hospital_network
        self.room_rent_limit = room_rent_limit

    def calculate_premium(self):

        return self.premium_amount + (self.premium_amount * 0.10)

    def display_policy(self):

        print("\n------Health Insurance------")
        print("Policy Id :", self.policy_id)
        print("Policy Name :", self.policy_name)
        print("Premium :", self.calculate_premium())
        print("Coverage :", self.coverage_amount)
        print("Hospital Network :", self.hospital_network)
        print("Room Rent Limit :", self.room_rent_limit)


class LifeInsurance(InsurancePolicy):

    def __init__(self,
                 policy_id,
                 policy_name,
                 premium_amount,
                 policy_duration,
                 coverage_amount,
                 nominee_name,
                 sum_assured):

        super().__init__(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount
        )

        self.nominee_name = nominee_name
        self.sum_assured = sum_assured

    def calculate_premium(self):

        return self.premium_amount + (self.premium_amount * 0.15)

    def display_policy(self):

        print("\n------Life Insurance------")
        print("Policy Id :", self.policy_id)
        print("Policy Name :", self.policy_name)
        print("Premium :", self.calculate_premium())
        print("Nominee :", self.nominee_name)
        print("Sum Assured :", self.sum_assured)


class VehicleInsurance(InsurancePolicy):

    def __init__(self,
                 policy_id,
                 policy_name,
                 premium_amount,
                 policy_duration,
                 coverage_amount,
                 vehicle_number,
                 vehicle_type,
                 vehicle_value):

        super().__init__(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount
        )

        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.vehicle_value = vehicle_value

    def calculate_premium(self):

        return self.premium_amount + (self.premium_amount * 0.20)

    def display_policy(self):

        print("\n------Vehicle Insurance------")
        print("Policy Id :", self.policy_id)
        print("Policy Name :", self.policy_name)
        print("Premium :", self.calculate_premium())
        print("Vehicle Number :", self.vehicle_number)
        print("Vehicle Type :", self.vehicle_type)
        print("Vehicle Value :", self.vehicle_value)


class SeniorCitizenHealthInsurance(HealthInsurance):

    def __init__(self,
                 policy_id,
                 policy_name,
                 premium_amount,
                 policy_duration,
                 coverage_amount,
                 hospital_network,
                 room_rent_limit,
                 age_limit,
                 annual_health_checkup):

        super().__init__(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount,
            hospital_network,
            room_rent_limit
        )

        self.age_limit = age_limit
        self.annual_health_checkup = annual_health_checkup

    def calculate_premium(self):

        return self.premium_amount + (self.premium_amount * 0.05)

    def display_policy(self):

        print("\n------Senior Citizen Health Insurance------")
        print("Policy Id :", self.policy_id)
        print("Policy Name :", self.policy_name)
        print("Premium :", self.calculate_premium())
        print("Age Limit :", self.age_limit)
        print("Annual Health Checkup :", self.annual_health_checkup)