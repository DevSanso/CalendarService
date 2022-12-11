import os
from config import BUILD_CONFIG,Config




def __get_go_grpc_package_path(root : str):
    return '(%s/pkg/grpc)' % root


def __build_protobuf(dirs : List[str], entrypoint : str,root_path : str):
    pass


def build_grpc(go_workspace : str,protobuf_workspace : str, cfg : Config):
    go_grpc_package = __get_go_grpc_package_path(go_workspace)
    
    if os.path.exists(go_grpc_package):
        os.mkdir(go_grpc_package)
    else:
        os.popen('rm -r %s/**' % go_grpc_package)
    
    entrypoint : str = cfg.grpc.entrypoint 
    __build_protobuf(os.listdir(go_grpc_package),entrypoint,go_grpc_package)    
    
