// FlatbufferGenerators.h

inline std::pair<std::unique_ptr<uint8_t[]>, size_t>
convert_to_raw_flatbuffer(nlohmann::json const &item) {
  std::string const schema = item["schema"];
  if (schema == "f144") {
    std::pair<std::unique_ptr<uint8_t[]>, size_t> f144_message =
        FlatBuffers::create_f144_message_double(
            item["source_name"], item["value"], item["timestamp"]);
    return f144_message;
  } else if (schema == "ep01") {
    ConnectionInfo connection_status;
    if (item["connection_status"] == "ConnectionInfo::CONNECTED") {
      connection_status = ConnectionInfo::CONNECTED;
    } else {
      connection_status = ConnectionInfo::DISCONNECTED;
    }
    std::pair<std::unique_ptr<uint8_t[]>, size_t> ep01_message =
        FlatBuffers::create_ep01_message_double(
            item["source_name"], connection_status, item["timestamp"]);
    return ep01_message;
  } else if (schema == "al00") {
    Severity severity;
    if (item["severity"] == "Severity::INVALID") {
      severity = Severity::INVALID;
    } else if (item["severity"] == "Severity::MAJOR") {
      severity = Severity::MAJOR;
    } else if (item["severity"] == "Severity::MINOR") {
      severity = Severity::MINOR;
    } else {
      severity = Severity::OK;
    }
    std::pair<std::unique_ptr<uint8_t[]>, size_t> al00_message =
        FlatBuffers::create_al00_message_double(
            item["source_name"], item["timestamp"], severity, item["message"]);
    return al00_message;
  } else if (schema == "ev44") {
    std::pair<std::unique_ptr<uint8_t[]>, size_t> ev44_message =
        FlatBuffers::create_ev44_message(
            item["source_name"], item["message_id"], item["reference_time"],
            item["time_of_flight"], item["pixel_ids"]);
    return ev44_message;
  } else if (schema == "ad00") {
    std::vector<std::vector<uint16_t>> data = item["data"];
    std::pair<std::unique_ptr<uint8_t[]>, size_t> ad00_message =
        FlatBuffers::create_ad00_message_uint16(item["source_name"], data,
                                                item["timestamp"]);
    return ad00_message;
  } else if (schema == "da00") {
    std::vector<int32_t> data = item["data"];
    std::pair<std::unique_ptr<uint8_t[]>, size_t> da00_message =
        FlatBuffers::create_da00_message_int32s(item["source_name"],
                                                item["name"], item["axis_name"],
                                                item["timestamp"], data);
    return da00_message;
  }
  throw std::runtime_error(fmt::format("Unknown schema {}", schema));
}