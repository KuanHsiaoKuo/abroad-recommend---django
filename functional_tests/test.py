from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import pdb
class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def testDown(self):
        self.browser.quit()
    def test_show_recommend_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn('海外推荐', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('今日推荐', header_text)
