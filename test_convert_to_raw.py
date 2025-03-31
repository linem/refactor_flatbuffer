import pytest

from convert_to_raw import convert_to_raw_flatbuffer


def test_f144_message():
    expected = "f144_raw_flatbuffer"
    item = {
        "schema": "f144",
        "source_name": "source",
        "value": "value",
        "timestamp": 0
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_ep01_message_connected():
    expected = "ep01_raw_flatbuffer_CONNECTED_unquoted"
    item = {
        "schema": "ep01",
        "source_name": "source",
        "connection_status": "CONNECTED",
        "timestamp": 0,
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_ep01_message_not_connected():
    expected = "ep01_raw_flatbuffer_DISCONNECTED_unquoted"
    item = {
        "schema": "ep01",
        "source_name": "source",
        "connection_status": "UNKNOWN",
        "timestamp": 0,
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_al00_message_major():
    expected = "al00_raw_flatbuffer_MAJOR_unquoted"
    item = {
        "schema": "al00",
        "source_name": "source",
        "timestamp": 0,
        "severity": "MAJOR",
        "message": "hello",
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected

def test_al00_message_ok():
    expected = "al00_raw_flatbuffer_OK_unquoted"
    item = {
        "schema": "al00",
        "source_name": "source",
        "timestamp": 0,
        "severity": "NONE",
        "message": "hello",
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_ad00_message():
    expected = "ad00_raw_flatbuffer"
    item = {
        "schema": "ad00",
        "source_name": "source",
        "data": "data",
        "timestamp": 0
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_da00_message():
    expected = "da00_raw_flatbuffer"
    item = {
        "schema": "da00",
        "source_name": "source",
        "name": "name",
        "axis_name": "axis_name",
        "timestamp": 0,
        "data": "data",
    }
    result = convert_to_raw_flatbuffer(item)
    assert result == expected


def test_unknown_message():
    item = {
        "schema": "xx99",
        "source_name": "source",
        "timestamp": 0,
        "data": "data"
    }
    with pytest.raises(ValueError):
        convert_to_raw_flatbuffer(item)
