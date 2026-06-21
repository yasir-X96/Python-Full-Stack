from models.insurance_policy import *

policies = []


def add_policy():

    print("\n-----Add Insurance Policy-----")

    print("1.Health Insurance")
    print("2.Life Insurance")
    print("3.Vehicle Insurance")
    print("4.Senior Citizen Health Insurance")

    choice = int(input("\nEnter Policy Type::"))

    policy_id = int(input("Enter Policy Id::"))
    policy_name = input("Enter Policy Name::")
    premium_amount = float(input("Enter Premium Amount::"))
    policy_duration = int(input("Enter Policy Duration::"))
    coverage_amount = float(input("Enter Coverage Amount::"))

    if choice == 1:

        hospital_network = input("Enter Hospital Network::")
        room_rent_limit = float(input("Enter Room Rent Limit::"))

        policy = HealthInsurance(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount,
            hospital_network,
            room_rent_limit
        )

    elif choice == 2:

        nominee_name = input("Enter Nominee Name::")
        sum_assured = float(input("Enter Sum Assured::"))

        policy = LifeInsurance(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount,
            nominee_name,
            sum_assured
        )

    elif choice == 3:

        vehicle_number = input("Enter Vehicle Number::")
        vehicle_type = input("Enter Vehicle Type::")
        vehicle_value = float(input("Enter Vehicle Value::"))

        policy = VehicleInsurance(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount,
            vehicle_number,
            vehicle_type,
            vehicle_value
        )

    elif choice == 4:

        hospital_network = input("Enter Hospital Network::")
        room_rent_limit = float(input("Enter Room Rent Limit::"))
        age_limit = int(input("Enter Age Limit::"))
        annual_health_checkup = input("Annual Health Checkup(True/False)::")

        policy = SeniorCitizenHealthInsurance(
            policy_id,
            policy_name,
            premium_amount,
            policy_duration,
            coverage_amount,
            hospital_network,
            room_rent_limit,
            age_limit,
            annual_health_checkup
        )

    else:
        print("Invalid Policy Type")
        return

    policies.append(policy)

    print("Insurance Policy Added Successfully")


def display_policies():

    if len(policies) == 0:
        print("\nNo Policies Found")
        return

    print("\n-----Display Policies-----")

    for policy in policies:
        policy.display_policy()


def create_policies():

    health = HealthInsurance(
        101,
        "Health Care",
        5000,
        1,
        500000,
        "Apollo",
        3000
    )

    life = LifeInsurance(
        102,
        "Life Secure",
        7000,
        10,
        1000000,
        "Shashank",
        1000000
    )

    vehicle = VehicleInsurance(
        103,
        "Vehicle Shield",
        4000,
        1,
        200000,
        "TS09AB1234",
        "Car",
        800000
    )

    senior = SeniorCitizenHealthInsurance(
        104,
        "Senior Care",
        9000,
        1,
        700000,
        "Apollo",
        5000,
        60,
        True
    )

    print("\n-----Single Inheritance-----")
    health.display_policy()

    print("\n-----Hierarchical Inheritance-----")
    life.display_policy()
    vehicle.display_policy()

    print("\n-----Multilevel Inheritance-----")
    senior.display_policy()


def demonstrate_polymorphism():

    health = HealthInsurance(
        101,
        "Health Care",
        5000,
        1,
        500000,
        "Apollo",
        3000
    )

    life = LifeInsurance(
        102,
        "Life Secure",
        7000,
        10,
        1000000,
        "Yasir",
        1000000
    )

    vehicle = VehicleInsurance(
        103,
        "Vehicle Shield",
        4000,
        1,
        200000,
        "TS09AB1234",
        "Car",
        800000
    )

    senior = SeniorCitizenHealthInsurance(
        104,
        "Senior Care",
        9000,
        1,
        700000,
        "Apollo",
        5000,
        60,
        True
    )

    policy_list = [
        health,
        life,
        vehicle,
        senior
    ]

    print("\n-----Polymorphism Demonstration-----")

    for policy in policy_list:
        policy.display_policy()