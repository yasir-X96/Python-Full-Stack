from app.policy_services import *


while True:

    print("\n=========== SecureLife 360 ===========")
    print("1. Add Policy Holder")
    print("2. Assign Policy Plan")
    print("3. Update Contact Details")
    print("4. Add Policy Benefits")
    print("5. Create Customer Profile")
    print("6. Search Policy")
    print("7. Delete Policy")
    print("8. Display All Policies")
    print("9. Premium Calculator")
    print("10. Process Claim")
    print("11. Get Policy Holders")
    print("12. Calculate Customer Age")
    print("13. Save Policies To File")
    print("14. Read Policies From File")
    print("15. Exit")

    choice = int(input("\nEnter Your Choice : "))

    try:
        if choice == 1:

            policy_id = int(input("Enter Policy ID : "))
            customer_name = input("Enter Customer Name : ")

            print("\nPolicy Types")
            print("1. Health Insurance")
            print("2. Vehicle Insurance")
            print("3. Life Insurance")
            print("4. Travel Insurance")

            type_choice = int(input("Enter Policy Type Choice : "))

            types = {
                1: "Health Insurance",
                2: "Vehicle Insurance",
                3: "Life Insurance",
                4: "Travel Insurance"
            }

            policy_type = types.get(type_choice)

            add_policy_holder(policy_id, customer_name, policy_type)

        elif choice == 2:

            policy_id = int(input("Enter Policy ID : "))
            plan = input("Enter Plan Name : ")
            premium = float(input("Enter Premium Amount : "))

            assign_policy_plan(policy_id, plan, premium)

        elif choice == 3:

            policy_id = int(input("Enter Policy ID : "))
            contact = input("Enter Contact Number : ")

            update_contact_details(policy_id, contact)

        elif choice == 4:

            policy_id = int(input("Enter Policy ID : "))
            benefit = input("Enter Benefit : ")

            add_policy_benefits(policy_id, benefit)

        elif choice == 5:

            policy_id = int(input("Enter Policy ID : "))
            dob = input("Enter DOB (dd-mm-yyyy) : ")

            create_customer_profile(policy_id, dob)

        elif choice == 6:

            policy_id = int(input("Enter Policy ID : "))

            search_policy(policy_id)

        elif choice == 7:

            policy_id = int(input("Enter Policy ID : "))

            delete_policy(policy_id)

        elif choice == 8:

            display_all_policies()

        elif choice == 9:

            premium_amount = float(input("Enter Premium Amount : "))
            tax_percent = float(input("Enter Tax Percentage : "))
            discount = float(input("Enter Discount : "))

            premium_calculator(
                premium_amount,
                tax_percent,
                discount
            )

        elif choice == 10:

            policy_id = int(input("Enter Policy ID : "))
            claim_amount = float(input("Enter Claim Amount : "))

            process_claim(policy_id, claim_amount)

        elif choice == 11:

            result = get_policy_holders()

            print("\n=========== POLICY HOLDERS ===========")
            print(result)

        elif choice == 12:

            dob = input("Enter DOB (dd-mm-yyyy) : ")

            calculate_customer_age(dob)

        elif choice == 13:

            save_policy_to_file()

        elif choice == 14:

            read_all_policies()

        elif choice == 15:

            print("\nThank You For Using SecureLife360")
            break


        else:
            print("\nInvalid Choice")

    except Exception as e:
        print(f"\nError : {e}")

    finally:
        print("\nOperation Completed")