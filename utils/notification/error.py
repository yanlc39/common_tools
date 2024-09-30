

class NotificationError(Exception):
	pass

class ProviderNotFound(NotificationError):
	pass

class ClientError(Exception):
	pass

class EmailClientLoginError(ClientError):
	pass