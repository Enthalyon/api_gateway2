from flask import Blueprint, request
import requests
from utils import load_file_config,  HEADERS


report_blueprints = Blueprint("report_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/report"


@report_blueprints.route("/report", methods=['GET'])
def get_highest_votes() -> dict:
    url = url_base + "/highest_votes"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/result_by_table", methods=['GET'])
def get_result_by_table() -> dict:
    url = url_base + "/result_by_table"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/insert",methods=['GET'])
def get_result_by_candidate() -> dict:
    url = url_base + "/result_by_candidate"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/report/result_by_politicalparty",methods=['GET'])
def get_result_by_candidate() -> dict:
    url = url_base + "/result_by_politicalparty"
    response = requests.get(url, headers=HEADERS)
    return response.json()





