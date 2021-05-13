

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_witch(self):    # 获取屏幕宽
        return self.driver.get_window_size()['witch']

    def get_height(self):   # 获取屏幕高
        return self.driver.get_window_size()['height']

    def get_url(self):  # 获取当前页的url
        return self.driver.current_url()

    def get_source(self):   # 获取当前页的源
        return self.driver.page_source()

    def screenshot(self, filename):    # 截图
        self.driver.swipe()
        return self.driver.get_screenshot_as_file(filename)