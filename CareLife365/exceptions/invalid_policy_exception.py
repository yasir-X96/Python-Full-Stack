class InvalidPolicyException(Exception):
    def __init__(self, message="Invalid Policy details provided"):
        super().__init__(message)
