from flask import Blueprint
import requests

from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-votos') + "/reports"


@reports_blueprints.route("/reports/table_results/all", methods=['GET'])
def report_students_enrollments() -> dict:
    url = f'{url_base}/student_enrollments/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/table_results/<string:id_>", methods=['GET'])
def report_students_enrollments_by_id(id_: str) -> dict:
    url = f'{url_base}/student_enrollments/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidate_results/all", methods=['GET'])
def report_course_enrollments() -> dict:
    url = f'{url_base}/course_enrollments/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidate_results/<string:id_>", methods=['GET'])
def report_course_enrollments_by_id(id_: str) -> dict:
    url = f'{url_base}/course_enrollments/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/tables_top_results", methods=['GET'])
def report_students_more_enrollments() -> dict:
    url = f'{url_base}/students_top_enrollments'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/politicalparty_results", methods=['GET'])
def report_department_enrollments() -> dict:
    url = f'{url_base}/department_enrollments'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/politicalparty_distribution", methods=['GET'])
def report_department_distribution() -> dict:
    url = f'{url_base}/department_distribution'
    response = requests.get(url, headers=HEADERS)
    return response.json()