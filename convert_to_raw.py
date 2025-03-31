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

def convert_to_raw_flatbuffer(item):
    schema = item["schema"]

    if schema == "f144":
        f144_message = create_f144_message_double(
            item["source_name"],
            item["value"],
            item["timestamp"]
        )
        return f144_message

    elif schema == "ep01":
        if item["connection_status"] == "CONNECTED":
            connection_status = "CONNECTED_unquoted"
        else:
            connection_status = "DISCONNECTED_unquoted"
        ep01_message = create_ep01_message_double(
            item["source_name"],
            connection_status,
            item["timestamp"]
        )
        return ep01_message

    elif schema == "al00":
        if item["severity"] == "INVALID":
            severity = "INVALID_unquoted"
        elif item["severity"] == "MAJOR":
            severity = "MAJOR_unquoted"
        elif item["severity"] == "MINOR":
            severity = "MINOR_unquoted"
        else:
            severity = "OK_unquoted"
        al00_message = create_al00_message_double(
            item["source_name"],
            item["timestamp"],
            severity,
            item["message"]
        )
        return al00_message

    elif schema == "ad00":
        data = item["data"]
        ad00_message = create_ad00_message_uint16(
            item["source_name"],
            data,
            item["timestamp"]
        )
        return ad00_message

    elif schema == "da00":
        data = item["data"]
        da00_message = create_da00_message_int32s(
            item["source_name"],
            item["name"],
            item["axis_name"],
            item["timestamp"],
            data,
        )
        return da00_message

    else:
        raise ValueError(f"Unknown schema {schema}")