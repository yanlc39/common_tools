from utils.notification.client import SendNotifyClient
from azure.identity import ClientSecretCredential
from typing import Union

class OutlookClient(SendNotifyClient):
	__scope_url = 'https://graph.microsoft.com/.default'
	__send_url = 'https://graph.microsoft.com/v1.0/users/{}/sendMail'
	__data: dict = {
		"Message": {
			"Subject": "",
			"Body": {
				"ContentType": "Text",
				"Content": "0xFFFFFFFF"
			},
			"ToRecipients": [
				{"EmailAddress": {"Address": ""}}
			]
		},
		"SaveToSentItems": "true"
	}
	__account: str
	__headers: dict = {
		'Authorization': '',
		'Content-Type': 'application/json'
	}
	__dest: str
	__credential: ClientSecretCredential

	def __init__(self, account: str, tenant_id: str, client_id: str, client_secret: str, dest: str):
		self.__credential = ClientSecretCredential(
			tenant_id=tenant_id,
			client_id=client_id,
			client_secret=client_secret
		)
		self.__dest = dest
		self.__account = account
		token = self.__credential.get_token(self.__scope_url).token

		self.__headers['Authorization'] = f'Bearer {token}'

	def send_msg(self, title: str, body: Union[str, tuple, list]):
		self.__data['Message']['Subject'] = title or 'New Mail'
		self.__data['Message']['Body']['Content'] = body or ' '
		self.__data['Message']['ToRecipients'][0]['EmailAddress']['Address'] = self.__dest or 'default@example.com'
		import requests
		requests.post(
			self.__send_url.format(self.__account),
			headers=self.__headers,
			json=self.__data
		)
