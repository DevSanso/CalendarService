import json
import os
import env
import copy


class Config(object):
    def __set_config_field(self, obj : object):
        raise Exception('config.py - __set_config_field : not implement method __Config class')
    def __init__(self,path : str):
        try:
            config_file = open(path,'r')
        except Exception as e:
            raise Exception('config.py - __Config.__init__ : %s' % str(e))
        obj = json.loads(config_file.read()) 
        self.__set_config_field(obj)


class __BuildConfig(Config):
    def __set_config_field(self, obj : object):
        self.grpc = {}
        copy.deepcopy(self.grpc, obj.grpc)

    

 def __init_build_config(s : str):
    return __BuildConfig(s)

BUILD_CONFIG =  __init_build_config('%s/config/build.json' % env.ROOT_WORKSPACE)




