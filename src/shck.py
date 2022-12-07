
import sys
import os
import io
import base64
import time
import urllib.request
import imagehash

from PIL import Image
from bs4 import BeautifulSoup


GPLAY_SCR_URL  = "http://scr.gplay.ro/"
WEBSERVER_WAIT = 30 #seconds

IMAGE_MARKER_VERSION = b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAUAHgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/ooooAKtWdhd38pjs7ae4kClikMZcgDqSB2qrW34d12bw34gsdWtWzJayq+OfmX+JfxGQaAM63sbu7WVre2mmEMZllMaFtiDqzY6D3NdNH4VtdN0iHUfEFzNC9zF59tp9tHvmaLoJJGPESHsSCT2FdJ4ssLHwdp+pz6XKkkfiR1+wiNsFLD5ZXHHTLlUwe0bVv67L4tuvHseu+D5ruTQ9SNvOktsx+zKqxqrLOB8q7dpBDYwO2c0AeUeGdAm8TeI7XRoHSJ7hjmR+kaqpZifoAT+FdJZ+GfDXiVbyz8P3+qNqVpbvNCt7GgS8VBllTaco2OQDn3qxrr3XhnxwfGPhy2hGlT6hMmnuu1o5tvyyAIDnacsB046VqC9sPCkl14hk0aHRNTktpYLLSxO8kpkkG1pHU/6qNBuwpAJzQBgw+GPDmi6ZpVz4pv9QgutViFxBDYxI32eEnCySFjk5wTtXnHfNZWv+DdU0jxXJoVvBJqNw3zwfZYjIZ4yu4MoXJPHJx0rrvEugan47sPC+reHbV78DTIdPuY4sH7NLHkEMP4VOcgnjg1tanptj4i1LVZrCa+1Sbw/p9ppy2ukzCOS8xw77trEoD2APTsOSAeZ6F4VvtW8XWnh64RrC7nlCMLlChj4ycg85wOh61txeGNA1RNbttNl1e01DSbWW6b7eibJBFwwO3BjbPAySM8V2VzY2mr+MPAWoakkllp8umiFJPtTL/pELSbYmlJ3Bs7BnIPpjtPaah4m1w6xp/xA0cWmitC8k2oPAbcwFATEFk6SjOAFyxPByecgHg1FFFABRRRQAUUUUAFFFFAFmd3dYldiwVMKD/CPvYHoMkn8aRJZNuxXZUkb5lU4BoooAcQVWJgzAk569D7VH/y1Cdmxk96KKAJEkkRAEkZRIMMFOARnH8qRJZElGx2VsH5lOD+YoooAcnyxDuM459+v8hRcTSkeU0rsiE7QWJxRRQBUooooAKKKKAP/2Q=='

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_Log():

    def __init__(self):

        pass

    def write(self,txt):

        print("--> {}".format(txt))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_List():

    def __init__(self):

        self.objects = []

    def add(self,obj):

        self.objects.append(obj)  

    def remove(self,obj):

        self.objects.remove(obj)  

    def remove_by_attribute(self,attribute,value):

        _item = self.find_by_attribute(attribute,value)

        if _item != None:

            self.remove(_item)

    def __repr__(self):

        return self.__print()

    def __str__(self):

        return self.__print()

    def __print(self):

        _txt = ""
        
        for obj in self.objects:

            _txt += str(obj)

        return _txt

    def __iter__(self):

        for obj in self.objects:

            yield obj

    def __getitem__(self,index):

        return self.objects[index]

    def __len__(self):

        return len(self.objects)

    def find_by_attribute(self,attribute,value):

        _object = None

        for _obj in self.objects:

            if getattr(_obj,attribute) == value:

                _object = _obj

        return _object

    def __add__(self,other):

        self.objects += other.objects

        return self

    def reverse(self):

        self.objects.reverse()

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_Html():

    def __init__(self):

        pass

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

    def to_safe_name(self,name):

        _safe_name = name

        _characters = ["\\/-+_"]

        for _character in _characters:
            _safe_name = _safe_name.replace(_character,"_")

        return _safe_name

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_Screenshot(SCHK_Html):

    def __init__(self):

        self.name    = ""
        self.url     = ""
        self.path    = ""
        self.image   = None
        self.is_dota = False

    def save(self):

        self.data.save(self.path)

    def load_from_file(self):

        self.image = Image.open(self.path)

        self.image.load()

    def load_from_html(self):

        _bytes = self.read_html_bytes(self.url)

        self.image = Image.open(io.BytesIO(_bytes))

    def to_base64(self,image):

        _buffer = io.BytesIO()

        image.save(_buffer, format="JPEG")

        return base64.b64encode(_buffer.getvalue())

    def from_base64(self,data):

        _bytes = base64.b64decode(data)

        image = Image.open(io.BytesIO(_bytes))

        return image

    def compare(self,image1,image2):

        _hash_1     = imagehash.average_hash(image1)
        _hash_2     = imagehash.average_hash(image2)
        _hash_limit = 5

        return (_hash_1 - _hash_2) < _hash_limit

    def is_dota_marker(self):

        _mk_vs_rect = (1760,10,1880,30)

        _img_mk_vs_1 = self.image.crop(_mk_vs_rect)

        _img_mk_vs_2 = self.from_base64(IMAGE_MARKER_VERSION)

        return self.compare(_img_mk_vs_1, _img_mk_vs_2)

    def process(self):

        self.is_dota = self.is_dota_marker()

    def __repr__(self):

        return self.__print()

    def __str__(self):

        return self.__print()

    def __print(self):

        _txt = "name [{}] path [{}] url [{}] \n".format(self.name,self.path,self.url)

        return _txt

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK_User(SCHK_Html):

    def __init__(self,name,log):

        SCHK_Html.__init__(self)

        self.name     = name
        self.url      = "{}/{}".format(GPLAY_SCR_URL,urllib.parse.quote(name))
        self.images   = SCHK_List()
        self.path_dw  = ""
        self.log      = log

        self.__create_dirs()

    def __create_dirs(self):

        _path_schk     = os.path.join(os.path.expanduser("~"),".schck")
        _path_schk_dw  = os.path.join(_path_schk,'dw')
        self.path_dw   = os.path.join(_path_schk_dw,self.to_safe_name(self.name))

        if not os.path.exists(_path_schk):

            os.mkdir(_path_schk)

        if not os.path.exists(_path_schk_dw):

            os.mkdir(_path_schk_dw)

        if not os.path.exists(_path_schk_dw):

            os.mkdir(_path_schk_dw)

        if not os.path.exists(self.path_dw):

            os.mkdir(self.path_dw)

    def __get_img_list(self):

        _images = []

        _html_str = self.read_html_str(self.url)

        _html_data = BeautifulSoup(_html_str, 'html.parser')

        _html_data.prettify()

        for _link in _html_data.pre.find_all('a'):

            _images.append(_link.get_text())

        _images = _images[1:]

        return _images

    def __get_img(self,image):

        _images = []

        _user_url = "{}".format(self.url,image)

        _html_bytes = self.read_html_bytes(_user_url)

        return _html_bytes

    def download(self):

        self.log.write("downloading screenshot list for user [{}]".format(self.name))

        _img_list = self.__get_img_list()

        self.log.write("found [{}] images".format(len(_img_list)))

        _count = 1

        for _img_name in _img_list:

            self.log.write("[{}/{}]downloading screenshot [{}] for user [{}]".format(_count,len(_img_list),_img_name,self.name))

            _img      = SCHK_Screenshot()
            _img.name = _img_name
            _img.url  = "{}/{}".format( self.url, urllib.parse.quote(_img_name) )
            _img.path = os.path.join( self.path_dw, _img_name )

            _img.load_from_html()

            _img.save()

            #wait to trick the web server
            time.sleep(WEBSERVER_WAIT)

            self.images.add(_img)

            _count += 1

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class SCHK():

    def __init__(self):

        self.log = SCHK_Log()

    def run(self):

        _user = SCHK_User("`Nameless`",self.log)
        _user.download()

    def get_html_user_list(self):

        _users = []

        _html_str = self.read_html_str(GPLAY_SCR_URL)

        _html_data = BeautifulSoup(_html_str, 'html.parser')

        _html_data.prettify()

        for _link in _html_data.pre.find_all('a'):

            _users.append(_link.get_text())

        return _users

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
if __name__ == '__main__':

    # SCHK().run()

    _img = SCHK_Screenshot()

    _img.path = r"c:\Users\stefa\.schck\dw\`Nameless`\01-09-2022 22-45-50.jpg"

    _img.load_from_file()

    _img.process()
