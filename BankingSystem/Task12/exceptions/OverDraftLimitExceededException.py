class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Withdrawal exceeds overdraft limit."):
        self.message = message
        super().__init__(self.message)
