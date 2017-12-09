import pymysql.cursors
from models.project import Project


class DbFixture():
    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, port=port, autocommit=True)
        self.connection.autocommit(True)

    def get_projects_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name FROM mantis_project_table")
            for row in cursor:
                (id, name) = row
                list.append(Project(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()