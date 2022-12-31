import os
import subprocess
from config import BUILD_CONFIG,BuildConfig
import benv



def __get_go_grpc_package_path(root : str):
    return '(%s/pkg/grpc)' % root

def __get_protoc_exec_source(protobuf_workspace : str
        , entrypoint_dir : str
        , output : str
        , entrypoint : str):
    return 'protoc -I %s -I %s --go_out=%s %s' % (protobuf_workspace
            , entrypoint_dir
            , output
            , entrypoint)



def exist_entrypoint(sdir : str,entrypoint :str):
    return os.path.exists(os.path.join(sdir,entrypoint))

def __execute_protoc(entrypoint_dir : str, output : str, entrypoint : str):
    source = __get_protoc_exec_source(benv.PROTOBUF_WORKSPACE, entrypoint_dir, output, entrypoint)
    ret = subprocess.call(source)
    if not ret == 0:
        raise Exception('subprocess call( %s  ) exception' % source)


def __build_protobuf_loop(protobuf_dirs : list[str], go_grpc_package : str, entrypoint : str):
    for protobuf_dir in protobuf_dirs:
        if not exist_entrypoint(protobuf_dir,entrypoint):
            _build_protobuf_loop(os.listdir(protobuf_dir),go_grpc_package,entrypoint)
            continue

        __execute_protoc(protobuf_dir, go_grpc_package, entrypoint)

        



def build_grpc(go_workspace : str,protobuf_workspace : str, cfg : BuildConfig):
    go_grpc_package = __get_go_grpc_package_path(go_workspace)
    
    if os.path.exists(go_grpc_package):
        os.mkdir(go_grpc_package)
    else:
        os.popen('rm -r %s/**' % go_grpc_package)
    
    entrypoint : str = cfg.grpc['entrypoint'] 
    
