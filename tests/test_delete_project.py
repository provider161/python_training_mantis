from models.project import Project
import random

def test_delete_random_project(app, db):
    app.open_manage_page()
    app.project.open_project_manage_page()
    if len(db.get_projects_list()) == 0:
        app.project.create_new_project()
        app.project.fill_project_form(Project(name="test", description="test"))
        app.project.submit_project_creation()
        app.project.open_project_manage_page()
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    app.project.select_project_by_id(project.id)
    app.project.delete_project()
    new_projects = db.get_projects_list()
    old_projects.remove(project)
    assert old_projects == new_projects