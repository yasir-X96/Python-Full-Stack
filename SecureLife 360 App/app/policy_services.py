from app.data import policies
from app.exceptions import InvalidPolicyID
from app.decorators import login_required


def add_policy_holder():

    policy_id = int(input("Enter Policy ID: "))
    name = input("Enter Customer Name: ")
    age = int(input("Enter Age: "))
    mobile = input("Enter Mobile Number: ")

    policies[policy_id] = {
        "name": name,
        "age": age,
        "mobile": mobile,
        "plan": "Not Assigned",
        "benefits": []
    }

    print("Policy Holder Added Successfully")


def assign_policy_plan():

    policy_id = int(input("Enter Policy ID: "))

    if policy_id in policies:
        plan = input("Enter Plan Name: ")
        policies[policy_id]["plan"] = plan
        print("Policy Plan Assigned Successfully")

    else:
        print("Invalid Policy ID")


def update_contact_details():

    policy_id = int(input("Enter Policy ID: "))

    if policy_id in policies:
        mobile = input("Enter New Mobile Number: ")
        policies[policy_id]["mobile"] = mobile
        print("Contact Updated Successfully")

    else:
        print("Invalid Policy ID")


def add_policy_benefits():

    policy_id = int(input("Enter Policy ID: "))

    if policy_id in policies:
        benefit = input("Enter Benefit: ")
        policies[policy_id]["benefits"].append(benefit)
        print("Benefit Added Successfully")

    else:
        print("Invalid Policy ID")


def create_customer_profile():

    policy_id = int(input("Enter Policy ID: "))

    if policy_id in policies:
        print("\nCustomer Profile")
        print(policies[policy_id])

    else:
        print("Invalid Policy ID")


def search_policy(policy_id):

    if policy_id in policies:
        print("\nPolicy Found")
        print(policies[policy_id])

    else:
        raise InvalidPolicyID("Policy ID Not Found")


def delete_policy():

    policy_id = int(input("Enter Policy ID: "))

    if policy_id in policies:
        del policies[policy_id]
        print("Policy Deleted Successfully")

    else:
        print("Invalid Policy ID")


def display_all_policies():

    if len(policies) == 0:
        print("No Policies Available")

    else:
        print("\nAll Policies")

        for policy_id, details in policies.items():
            print(f"\nPolicy ID : {policy_id}")
            print(details)


@login_required
def premium_calculator():

    premium_amount = float(input("Enter Premium Amount: "))
    tax_percent = float(input("Enter Tax Percentage: "))
    discount = float(input("Enter Discount Amount: "))

    final_premium = (
        premium_amount +
        (premium_amount * tax_percent / 100)
    ) - discount

    print(f"Final Premium Amount = {final_premium}")