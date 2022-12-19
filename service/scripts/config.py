import json
import os
import benv
import copy
from abc import abstractmethod

class Config(object):
    @abstractmethod
    def __set_config_field(self, obj : dict):
        raise Exception('config.py - __set_config_field : not implement method __Config class')
    def __init__(self,path : str):
        try:
            config_file = open(path,'r')
        except Exception as e:
            raise Exception('config.py - __Config.__init__ : %s' % str(e))
        obj = json.loads(config_file.read()) 
        self.__set_config_field(obj)


class BuildConfig(Config):
    grpc : dict = {}

    def __set_config_field(self, obj :dict):
        copy.deepcopy(self.grpc, obj['grpc'])

    

def __init_build_config(s : str):
    return BuildConfig(s)

BUILD_CONFIG = __init_build_config('%s/config/build.json' % benv.ROOT_WORKSPACE)




