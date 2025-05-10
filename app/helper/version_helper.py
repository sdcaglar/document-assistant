import json


def get_version(BASE_DIR):
    with open(BASE_DIR + "/rpmvenv_config.json") as json_file:
        return json.load(json_file)["core"]["version"]


def get_release_no(BASE_DIR):
    with open(BASE_DIR + "/rpmvenv_config.json") as json_file:
        return json.load(json_file)["core"]["release"]
