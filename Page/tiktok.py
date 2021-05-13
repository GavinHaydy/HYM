from Business.BaseUtil import BasePage


class Browser(BasePage):
    def i_know(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/ect').click()

    def agree(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/af7').click()

    def before_login(self):
        self.by_partial_link_text('我').click()

    def password_login(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/byr').click()

    def phone_num(self, phone):
        self.by_id('com.ss.android.ugc.aweme.lite:id/ccz').send_keys(phone)

    def password(self, password):
        self.by_id('com.ss.android.ugc.aweme.lite:id/cby').send_keys(password)

    def user_agree(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/cl_').click()

    def login(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/bzp').click()

    def skip(self):
        self.by_id('com.ss.android.ugc.aweme.lite:id/d8v').click()