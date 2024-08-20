import json


def load_request_log():
  with open("request_logs.json", "r") as f:
    request_log = json.loads("[" + f.read().replace("]\n[", "],\n[") + "]")

  return request_log
