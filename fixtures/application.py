from selenium import webdriver
from fixtures.session import SessionHelper

class Application:

    def __init__(self, browser, base_url):
        #self.wd.implicitly_wait(5)
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser '%s'" % browser)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()