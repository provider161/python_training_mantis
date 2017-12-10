from models.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:
    def __init__(self, app):
        self.app = app


    def get_projects_list(self, username, password):
        list = []
        client = Client("http://localhost:8888/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return False
        for project in projects:
            list.append(Project(id = project.id, name=project.name))
        return list