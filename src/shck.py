
import sys
import os
import urllib.request
from bs4 import BeautifulSoup


GPLAY_SCR_URL = "http://scr.gplay.ro/"

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
class SCHK_Image():

    def __init__(self):

        self.name = ""
        self.url  = ""
        self.path = ""
        self.data = None

    def save(self):

        with open(self.path,'wb+') as _image:

            _image.write(self.data)

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

            _img      = SCHK_Image()
            _img.name = _img_name
            _img.url  = "{}/{}".format( self.url, urllib.parse.quote(_img_name) )
            _img.path = os.path.join( self.path_dw, _img_name )

            _img.data = self.read_html_bytes(_img.url)

            _img.save()

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

    SCHK().run()