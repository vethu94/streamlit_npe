import json
import os

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "../config.json"), "r") as jsonfile:
    config = json.load(jsonfile)


def get_config():
    return config
