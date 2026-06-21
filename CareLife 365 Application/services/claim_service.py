from models.insurance_claim import *

claims = []


def add_claim():

    print("\n------Add Claim------")

    claim_id = int(input("Enter Claim Id       : "))
    claim_amount = float(input("Enter Claim Amount   : "))
    claim_status = input("Enter Claim Status   : ")
    hospital_name = input("Enter Hospital Name  : ")

    claim = InsuranceClaim(
        claim_id,
        claim_amount,
        claim_status,
        hospital_name
    )

    claims.append(claim)

    print("\nClaim Added Successfully")


def display_claims():

    if len(claims) == 0:
        print("\nNo Claims Found")
        return

    print("\n------Claim List------")

    for claim in claims:
        claim.display_claim_details()


def create_claims():

    print("\n------Insurance Claim Objects------")

    claim1 = InsuranceClaim(
        201,
        25000,
        "Pending",
        "Apollo Hospital"
    )

    claim2 = InsuranceClaim(
        202,
        40000,
        "Approved",
        "Yashoda Hospital"
    )

    claim1.display_claim_details()
    claim2.display_claim_details()

    print("\n------Health Claim------")

    health_claim = HealthClaim(
        301,
        30000,
        "Pending",
        "Apollo Hospital",
        "Viral Fever"
    )

    health_claim.display_health_claim()

    print("\n------Vehicle Claim------")

    vehicle_claim = VehicleClaim(
        302,
        50000,
        "Approved",
        "N/A",
        "Hyderabad",
        40000
    )

    vehicle_claim.display_vehicle_claim()