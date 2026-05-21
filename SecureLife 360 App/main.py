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
    print("10. Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_policy_holder()

        elif choice == 2:
            assign_policy_plan()

        elif choice == 3:
            update_contact_details()

        elif choice == 4:
            add_policy_benefits()

        elif choice == 5:
            create_customer_profile()

        elif choice == 6:

            try:
                policy_id = int(input("Enter Policy ID: "))
                search_policy(policy_id)

            except Exception as e:
                print(e)

        elif choice == 7:
            delete_policy()

        elif choice == 8:
            display_all_policies()

        elif choice == 9:
            premium_calculator()

        elif choice == 10:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter Numbers Only")