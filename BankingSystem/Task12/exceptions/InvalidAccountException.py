class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number provided."):
        self.message = message
        super().__init__(self.message)
