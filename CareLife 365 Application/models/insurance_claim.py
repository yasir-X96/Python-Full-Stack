class InsuranceClaim:

    def __init__(self,
                 claim_id,
                 claim_amount,
                 claim_status,
                 hospital_name):

        self.claim_id = claim_id
        self.claim_amount = claim_amount
        self.claim_status = claim_status
        self.hospital_name = hospital_name

    def display_claim_details(self):

        print("\n------Claim Details------")
        print("Claim Id         :", self.claim_id)
        print("Claim Amount     :", self.claim_amount)
        print("Claim Status     :", self.claim_status)
        print("Hospital Name    :", self.hospital_name)

    def __str__(self):

        return (f"InsuranceClaim("
                f"Id={self.claim_id}, "
                f"Amount={self.claim_amount})")


class HealthClaim(InsuranceClaim):

    def __init__(self,
                 claim_id,
                 claim_amount,
                 claim_status,
                 hospital_name,
                 disease_name):

        super().__init__(
            claim_id,
            claim_amount,
            claim_status,
            hospital_name
        )

        self.disease_name = disease_name

    def display_health_claim(self):

        self.display_claim_details()
        print("Disease Name     :", self.disease_name)


class VehicleClaim(InsuranceClaim):

    def __init__(self,
                 claim_id,
                 claim_amount,
                 claim_status,
                 hospital_name,
                 accident_location,
                 vehicle_damage_cost):

        super().__init__(
            claim_id,
            claim_amount,
            claim_status,
            hospital_name
        )

        self.accident_location = accident_location
        self.vehicle_damage_cost = vehicle_damage_cost

    def display_vehicle_claim(self):

        self.display_claim_details()
        print("Accident Location:", self.accident_location)
        print("Damage Cost      :", self.vehicle_damage_cost)