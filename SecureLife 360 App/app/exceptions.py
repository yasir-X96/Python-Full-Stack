class PolicyNotFoundException(Exception):
    pass


class DuplicatePolicyException(Exception):
    pass


class MissingCustomerDataException(Exception):
    pass


class InvalidPremiumException(Exception):
    pass


class InvalidPolicyTypeException(Exception):
    pass


class ClaimLimitExceededException(Exception):
    pass