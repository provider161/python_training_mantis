from models.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_css_selector("input.button-small[value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()

    def fill_project_form(self, Project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(Project.name)
        wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[4]/td[2]").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(Project.description)

    def submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Proceed").click()


    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()