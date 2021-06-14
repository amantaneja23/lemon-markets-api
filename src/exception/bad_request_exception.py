class BadRequestException(Exception):
	def __init__(self, validation_errors):
		self.validation_errors = validation_errors
		super().__init__(self.validation_errors)
