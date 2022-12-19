import os

def __init_env(e : str):
    val = os.getenv(e)
    if val == None:
        raise Exception('%s  - %s -> not exist os env(%s)' % ('env.py','__init_env',e))

    return val


ROOT_WORKSPACE = __init_env('CALENDAR_SERVICE_WORKSPACE')
PROTOBUF_WORKSPACE = __init_env('CALENDAR_PROTOBUF_WORKSPACE')

