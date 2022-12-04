
import sys
import os
import urllib.request


GPLAY_SCR_URL = "http://scr.gplay.ro/"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK():

	def __init__(self):

		pass

	def run(self):

		_html = SCHK_HTML()

		_data = _html.read(GPLAY_SCR_URL)

		print(_data)

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_HTML():

	def __init__(self):

		pass

	def read(self,url):

		_request = urllib.request.urlopen(url)
		_bytes   = _request.read()
		_data    = _bytes.decode("utf8")
		_request.close()

		return _data


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
if __name__ == '__main__':

	SCHK().run()