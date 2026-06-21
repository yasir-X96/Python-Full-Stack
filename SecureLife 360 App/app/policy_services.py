from datetime import datetime
def get_policy_holders():

    result = {
        policy_id: {
            "customer_name": details["customer_name"],
            "policy_type": details["policy_type"],
            "premium_amount": details["premium_amount"]
        }
        for policy_id, details in policies.items()
    }

    return result


def calculate_customer_age(date_of_birth):

    dob = datetime.strptime(date_of_birth, "%d-%m-%Y")

    today = datetime.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print(f"\nCustomer Age : {age} years")


def save_policy_to_file():

    with open("policies.txt", "w") as file:

        for policy_id, details in policies.items():
            file.write(f"Policy ID : {policy_id}\n")

            for key, value in details.items():
                file.write(f"{key} : {value}\n")

            file.write("----------------------------------\n")

    print("\nPolicy Data Saved Successfully")


def read_all_policies():

    try:
        with open("policies.txt", "r") as file:

            data = file.readlines()

            print("\n=========== FILE DATA ===========")

            for line in data:
                print(line.strip())

    except FileNotFoundError:
        print("\nNo File Found")