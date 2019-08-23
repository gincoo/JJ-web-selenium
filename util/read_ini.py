# coding=utf-8
import configparser
import os

path = os.path.abspath(os.path.dirname(os.getcwd() + '/config/LocalElement.ini'))

# .ini文件操作工具类
# 封装configparser框架
class ReadIni(object):

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = path
        if node is None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        """
        获取.ini文件对应节点node下,key对应的value
        :param key: ini文件
        :return: 返回value 值
        """
        data = self.cf.get(self.node, key)
        return data

# if __name__ == '__main__':
#    read_init = ReadIni()
#    print(read_init.get_value('user_name'))
