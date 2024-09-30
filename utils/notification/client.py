from abc import abstractmethod
from typing import Union


class SendNotifyClient(object):
	@abstractmethod
	def send_msg(self, title: str, content: Union[str, tuple, list]):
		pass
