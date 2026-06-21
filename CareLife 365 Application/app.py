from models.policy_holder import PolicyHolder
from services.policy_service import *
from services.claim_service import *
from services.premium_service import *

policyholders = []

print("Application Started")

while True:

    print("\n-----Welcome to CareLife365-----")
    print("1.AddPolicyHolder")
    print("2.UpdateMobileNumber")
    print("3.AddInsurancePolicy")
    print("4.AddInsuranceClaim")
    print("5.DisplayPolicyHolders")
    print("6.DisplayPolicies")
    print("7.DisplayClaims")
    print("8.DisplayPolicyTypes")
    print("9.PremiumCustomer")
    print("10.PolymorphismDemo")
    print("11.Exit")

    choice = int(input("\nEnter your Choice::"))

    if choice == 1:

        print("\n-----Add Policy Holder-----")

        pid = int(input("Enter Policy Holder Id::"))
        name = input("Enter Name::")
        age = int(input("Enter Age::"))
        mobile = input("Enter Mobile Number::")
        city = input("Enter City::")

        holder = PolicyHolder(
            pid,
            name,
            age,
            mobile,
            city
        )

        policyholders.append(holder)

        print("Policy Holder Added Successfully")

    elif choice == 2:

        print("\n-----Update Mobile Number-----")

        pid = int(input("Enter Policy Holder Id::"))
        mobile = input("Enter New Mobile Number::")

        found = False

        for holder in policyholders:

            if holder.policy_holder_id == pid:

                holder.update_mobile_number(mobile)
                found = True
                break

        if not found:
            print("Policy Holder Not Found")

    elif choice == 3:

        add_policy()

    elif choice == 4:

        add_claim()

    elif choice == 5:

        print("\n-----Display Policy Holders-----")

        if len(policyholders) == 0:
            print("No Policy Holders Found")

        else:
            for holder in policyholders:
                holder.display_policyholder()

    elif choice == 6:

        display_policies()

    elif choice == 7:

        display_claims()

    elif choice == 8:

        create_policies()

    elif choice == 9:

        create_premium_customer()

    elif choice == 10:

        demonstrate_polymorphism()

    elif choice == 11:

        print("\nThank You For Using CareLife365")
        print("Application Closed")
        break

    else:

        print("Invalid Choice")