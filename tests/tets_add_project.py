from models.project import Project

"""def test_add_project(app, db):
    project = Project(name="teasddst", description="test")
    app.open_manage_page()
    app.project.open_project_manage_page()
    old_projects = db.get_projects_list()
    app.project.create_new_project()
    app.project.fill_project_form(project)
    app.project.submit_project_creation()
    new_projects = db.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    app.project.open_project_manage_page()"""

def test_add_project(app, config):
    project = Project(name="teasdm,n,", description="test")
    app.open_manage_page()
    app.project.open_project_manage_page()
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    old_projects = app.soap.get_projects_list(username, password)
    app.project.create_new_project()
    app.project.fill_project_form(project)
    app.project.submit_project_creation()
    new_projects = app.soap.get_projects_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    app.project.open_project_manage_page()