class ClaimException(Exception):
    def __init__(self, message="Error in Claim Processing"):
        super().__init__(message)
