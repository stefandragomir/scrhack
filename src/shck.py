
import sys
import os
import urllib.request
from bs4 import BeautifulSoup


GPLAY_SCR_URL = "http://scr.gplay.ro/"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK():

	def __init__(self):

		self.users = []

	def run(self):

		_image = self.get_user_img("ghettosmurf","01-09-2022%2020-31-30.jpg")

		with open(r"c:\temp\img1.jpg",'wb+') as file:

			file.write(_image)

	def read_html_str(self,url):

		_request = urllib.request.urlopen(url)
		_bytes   = _request.read()
		_data    = _bytes.decode("utf8")
		_request.close()

		return _data

	def read_html_bytes(self,url):

		_request = urllib.request.urlopen(url)
		_bytes   = _request.read()
		_request.close()

		return _bytes

	def get_html_user_list(self):

		_users = []

		_html_str = self.read_html_str(GPLAY_SCR_URL)

		_html_data = BeautifulSoup(_html_str, 'html.parser')

		_html_data.prettify()

		for _link in _html_data.pre.find_all('a'):

			_users.append(_link.get_text())

		return _users

	def get_html_user_img_list(self,user):

		_images = []

		_user_url = "{}/{}".format(GPLAY_SCR_URL,user)

		_html_str = self.read_html_str(_user_url)

		_html_data = BeautifulSoup(_html_str, 'html.parser')

		_html_data.prettify()

		for _link in _html_data.pre.find_all('a'):

			_images.append(_link.get_text())

		_images = _images[1:]

		return _images

	def get_html_user_img(self,user,image):

		_images = []

		_user_url = "{}/{}/{}".format(GPLAY_SCR_URL,user,image)

		_html_bytes = self.read_html_bytes(_user_url)

		return _html_bytes

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
if __name__ == '__main__':

	SCHK().run()