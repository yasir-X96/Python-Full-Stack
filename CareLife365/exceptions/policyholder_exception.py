class PolicyHolderException(Exception):
    def __init__(self, message="Invalid PolicyHolder details"):
        super().__init__(message)
