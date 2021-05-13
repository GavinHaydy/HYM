from appium import webdriver
import unittest
from Page.tiktok import Browser
from time import sleep


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        print('开始')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities={
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.ss.android.ugc.aweme.lite',
            'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
        })

    def test_case(self,):
        page = Browser(self.driver)
        sleep(5)
        page.agree()
        sleep(7)
        page.driver.swipe(707, 443, 707, 444)
        sleep(2)
        page.driver.swipe(707, 443, 707, 444)
        # page.driver.back()
        # page.before_login()
        page.driver.swipe(810, 1540, 811, 1541)
        page.password_login()
        sleep(1)
        page.phone_num()    # 手机号
        sleep(5)
        page.password()   # 密码
        page.user_agree()
        page.login()
        sleep(3)
        page.skip()
        while True:
            page.driver.swipe(300, 1100, 300, 350)
            sleep(5)

    def tearDown(self) -> None:
        print('结束')
# 707 443