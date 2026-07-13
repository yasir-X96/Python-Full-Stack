from models.policy_holder import *

premium_customers = []


def create_premium_customer():

    customer = PremiumPolicyHolder(
        1,
        "Yasir",
        22,
        "9876543210",
        "Hyderabad",
        500,
        10
    )

    premium_customers.append(customer)

    customer.display_customer_profile()

    amount = 10000

    discount = customer.calculate_discount(amount)

    print("\nPremium Amount :", amount)
    print("Discount       :", discount)
    print("Final Amount   :", amount - discount)


def add_premium_customer():

    print("\n------Add Premium Customer------")

    pid = int(input("Enter Policy Holder Id : "))
    name = input("Enter Name             : ")
    age = int(input("Enter Age              : "))
    mobile = input("Enter Mobile Number    : ")
    city = input("Enter City             : ")

    points = int(input("Enter Loyalty Points   : "))
    discount = float(input("Enter Discount %       : "))

    customer = PremiumPolicyHolder(
        pid,
        name,
        age,
        mobile,
        city,
        points,
        discount
    )

    premium_customers.append(customer)

    print("\nPremium Customer Added Successfully")