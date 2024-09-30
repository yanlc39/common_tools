from typing import Union

import requests
from utils.notification.client import SendNotifyClient


class QQBot(SendNotifyClient):
	__send_url: str
	__data: dict = {
		"token": "",
		"title": "",
		"content": ""
	}

	def __init__(self, token: str, send_url: str, dest: str):
		self.__data['token'] = token
		self.__send_url = send_url
		self.__data['data'] = dest

	def send_msg(self, title: str, content: Union[str, tuple, list]):
		self.__data['title'] = title
		self.__data['content'] = content


		requests.post(url=self.__send_url, json=self.__data, verify=False)