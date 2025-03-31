
def create_f144_message_double(source_name, value, timestamp):
    return "f144_raw_flatbuffer"

def create_ep01_message_double(source_name, connection_status, timestamp):
    return f"ep01_raw_flatbuffer_{connection_status}"

def create_al00_message_double(source_name, timestamp, severity, message):
    return f"al00_raw_flatbuffer_{severity}"

def create_ad00_message_uint16(source_name, data, timestamp):
    return "ad00_raw_flatbuffer"

def create_da00_message_int32s(source_name, name, axis_name, timestamp, data):
    return "da00_raw_flatbuffer"