from flask import Blueprint, request
import requests
from utils import load_file_config,HEADERS

politicalParty_blueprints = Blueprint("politicalParty_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/politicalParty"


@politicalParty_blueprints.route("/politicalParty", methods=['GET'])
def get_all_politicalParty() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@politicalParty_blueprints.route("/politicalParty/<string:id_>", methods=['GET'])
def get_politicalParty_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@politicalParty_blueprints.route("/politicalParty/insert", methods=['POST'])
def insert_politicalParty() -> dict:
    politicalParty = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS,json=politicalParty)
    return response.json()


@politicalParty_blueprints.route("/politicalParty/update/<string:id_>",methods=['PUT'])
def update_politicalParty(id_: str) -> dict:
    politicalParty = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.post(url, headers=HEADERS, json=politicalParty)
    return response.json()


@politicalParty_blueprints.route("/politicalParty/delete/<string:id_>", methods=['DELETE'])
def delete_student(id_: str) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()




