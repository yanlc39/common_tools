from typing import Union

import requests
from utils.notification.client import SendNotifyClient

class TelegramBot(SendNotifyClient):
	__send_url: str
	__dest: str

	def __init__(self, bot_id, bot_key, send_url, dest):
		self.__send_url = f'{send_url}/{bot_id}:{bot_key}/sendMessage'
		self.__dest = dest

	def send_msg(self, title: str, content: Union[str, tuple, list]):
		data = {
			'chat_id': self.__dest,
			'text': title + str(content)
		}
		requests.get(url=self.__send_url, params=data, verify=False)

