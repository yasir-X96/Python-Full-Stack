from models.policy_holder import PolicyHolder
from models.premium_policy_holder import PremiumPolicyHolder
from models.insurance_claim import InsuranceClaim
from models.health_insurance import HealthInsurance
from models.life_insurance import LifeInsurance
from models.vehicle_insurance import VehicleInsurance
from models.senior_citizen_health_insurance import SeniorCitizenHealthInsurance
from services.policy_service import PolicyService
from services.claim_service import ClaimService
from utils.logger_util import log

def main():
    # Policy Holders
    yasir = PolicyHolder(1, "Yasir", 35, "9876543210", "Chennai")
    ratna = PremiumPolicyHolder(2, "Ratna", 40, "9123456780", "Hyderabad", loyalty_points=120, discount_percentage=10)

    # Policies
    health_policy = HealthInsurance("H101", "Health Basic", 15000, 5, 500000, "Apollo", 5000)
    life_policy = LifeInsurance("L201", "Life Secure", 20000, 10, 1000000, "Ratna", 1000000)
    vehicle_policy = VehicleInsurance("V301", "Car Protect", 12000, 3, 300000, "TS09AB1234", "Car", 800000)
    senior_policy = SeniorCitizenHealthInsurance("S401", "Senior Care", 18000, 4, 400000, "Fortis", 7000, 60, True)

    # Claims
    claim1 = InsuranceClaim("C101", 50000, "Approved", "Apollo")
    claim2 = InsuranceClaim("C102", 75000, "Pending", "Fortis")

    # Save Data
    policy_service = PolicyService()
    claim_service = ClaimService()

    policy_service.save_policies([health_policy, life_policy, vehicle_policy, senior_policy])
    claim_service.save_claims([claim1, claim2])
    log("Policies and Claims saved successfully.")

    # Display Policy Holders
    print(yasir)
    print(ratna)

    # Display Claims
    print(claim1)
    print(claim2)

    # Display Policies + Premiums
    print(health_policy.display_policy())
    print("Calculated Premium:", health_policy.calculate_premium())

    print(life_policy.display_policy())
    print("Calculated Premium:", life_policy.calculate_premium())

    print(vehicle_policy.display_policy())
    print("Calculated Premium:", vehicle_policy.calculate_premium())

    print(senior_policy.display_policy())
    print("Calculated Premium:", senior_policy.calculate_premium())

    # Premium PolicyHolder Discount
    print(ratna.display_customer_profile())
    discounted = ratna.calculate_discount(life_policy.premium_amount)
    print(f"Discounted Premium for Ratna: {discounted}")

if __name__ == "__main__":
    main()
