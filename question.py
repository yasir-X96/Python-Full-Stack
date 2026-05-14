# Assignment - 1

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


# Assignment - 2

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