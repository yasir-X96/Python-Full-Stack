#  Assignment - 1

# Question - 1
policy_number=67
customer_name="Yasir"
premium_amount=58620.67
policy_active_staus=True

print(f"policy numbe::{policy_number}\ncustomer name::{customer_name}\npremium amount::{premium_amount}\npolicy active staus::{policy_active_staus}")

# Question - 2
insurance_company_name="CMR Group"
policy_type="Health Insurance"
claim_status="Approved"
branch_location="medchal"

print(insurance_company_name)
print(policy_type)
print(claim_status)
print(branch_location)

# Question - 3
agent_name=None

print(agent_name)
print(type(agent_name))


# # Assignment - 2

policy_features=["Accidental Coverage","health coverage","Vechile Coverage","roadside assistance"]
print(policy_features)

policy_features.append("Cashless Garage");
print(policy_features);

#1.1
policy_features=["Accidental Coverage","health coverage","Vechile Coverage","roadside assistance","Cashless Garage"]
policy_features.remove("Cashless Garage");
print(policy_features);

#1.2
# #policy_features.count("health coverage");
# print(policy_features)

# Tuple
office_location=("chennai","Tamilnadu");
print(office_location);

# Set Data Type
unique_policy_ids={"101","102","103","101","102"}
print(unique_policy_ids)

# Dictionary
customer_details={
    "customer_id":501,
    "customer_name":"Priya",
    "policy_type":"health insurance",
    "premium":25000
}
print(customer_details)
print(customer_details["customer_name"])

#4.2
customer_details["premium"]=25000
print(customer_details)
print(customer_details.get("premium"))


# Assignment - 3

# Question 1 — Premium Calculator

customer_name = input("Enter Customer Name: ")
base_premium = float(input("Enter Base Premium Amount: "))
gst_percentage = 18

gst_amount = (base_premium * gst_percentage) / 100
final_premium = base_premium + gst_amount

print("Premium Details")
print("Customer Name:", customer_name)
print("Base Premium:", base_premium)
print("GST Amount:", gst_amount)
print("Final Premium:", final_premium)

# Question 2 — Insurance Discount System

age = int(input("Enter Customer Age: "))
premium_amount = float(input("Enter Premium Amount: "))

if age >= 60:
    discount = 20
elif age >= 40:
    discount = 10
else:
    discount = 0

discount_amount = (premium_amount * discount) / 100
final_payable = premium_amount - discount_amount

print("Discount Details")
print("Discount Percentage:", discount, "%")
print("Final Payable Premium:", final_payable)

# Question 3 — Policy Search System

policies = ["Health Insurance", "Vehicle Insurance", "Life Insurance"]

print("Available Policies:")
for policy in policies:
    print(policy)

search_policy = input("\nEnter policy to search: ")

found = False

for policy in policies:
    if policy == search_policy:
        found = True
        break

if found:
    print("Policy Found")
else:
    print("Policy Not Found")

# ASsignment 4

# Insurance Management System

# Question 1
# Global Collections

policy_holders = {}
policy_types = set()
claims = []


# Question 2
# Add Policy Holder Function

def add_policy_holder(policy_id, customer_name, policy_type):

    policy_holders[policy_id] = {
        "policy_id": policy_id,
        "customer_name": customer_name,
        "policy_type": policy_type,
        "plan": "Not Assigned",
        "premium_amount": 0,
        "nominee_details": {},
        "contact_details": (),
        "add_on_benefits": set(),
        "claim_history": []
    }

    # Add policy type into set
    policy_types.add(policy_type)

    print("Customer Details Added Successfully")
    print(policy_holders[policy_id])


# Function Call using positional arguments
add_policy_holder(101, "Rahul Sharma", "Health Insurance")


# Question 3
# Assign Policy Plan

def assign_policy_plan(policy_id, plan="Basic", premium=500):

    if policy_id in policy_holders:

        policy_holders[policy_id]["plan"] = plan
        policy_holders[policy_id]["premium_amount"] = premium

        print("\nUpdated Policy Details")
        print(policy_holders[policy_id])

    else:
        print("Policy ID not found")


# Call using default values
assign_policy_plan(101)

# Call by overriding default values
assign_policy_plan(101, "Premium", 1500)

# Question 4
# Update Contact Details

def update_contact(policy_id, email, phone, city):

    if policy_id in policy_holders:

        # Store contact details inside tuple
        policy_holders[policy_id]["contact_details"] = (
            email,
            phone,
            city
        )

        print("\nContact Details")

        contact = policy_holders[policy_id]["contact_details"]

        # Tuple indexing
        print("Email :", contact[0])
        print("Phone :", contact[1])
        print("City  :", contact[2])

    else:
        print("Policy ID not found")


# Function Call using keyword arguments
update_contact(
    policy_id=101,
    email="rahul@gmail.com",
    phone="9876543210",
    city="Hyderabad"
)

# Question 5
# Add Policy Benefits

def add_policy_benefits(policy_id, *benefits):

    if policy_id in policy_holders:

        # Store benefits inside set
        for benefit in benefits:
            policy_holders[policy_id]["add_on_benefits"].add(benefit)

        print("\nAll Benefits")
        print(policy_holders[policy_id]["add_on_benefits"])

    else:
        print("Policy ID not found")


# Pass multiple benefits
add_policy_benefits(
    101,
    "Roadside Assistance",
    "Accidental Cover",
    "Cashless Garage"
)

# Pass benefits using list unpacking
benefit_list = ["Roadside Assistance", "Accidental Cover"]

add_policy_benefits(101, *benefit_list)

# Question 6
# Create Customer Profile

def create_customer_profile(policy_id, **extra_info):

    if policy_id in policy_holders:

        # Use update()
        policy_holders[policy_id].update(extra_info)

        print("\nCustomer Extra Information")

        # Print key-value pairs
        for key, value in extra_info.items():
            print(key, ":", value)

    else:
        print("Policy ID not found")


# Function Call
create_customer_profile(
    101,
    age=30,
    annual_income=750000,
    marital_status="Married",
    occupation="Software Engineer",
    medical_history="No major illness"
)


# Question 7
# Display All Policies

def display_all_policies():

    print("\n====== ALL POLICY HOLDERS ======\n")

    for policy_id, details in policy_holders.items():

        print("Policy ID      :", policy_id)
        print("Customer Name  :", details["customer_name"])
        print("Policy Type    :", details["policy_type"])
        print("Premium Amount :", details["premium_amount"])
        print("Benefits       :", details["add_on_benefits"])
        print("-" * 40)


# Function Call
display_all_policies()