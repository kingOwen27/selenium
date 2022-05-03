from base import BasePage
class BaiduPage(BasePage):
    url="https://www.baidu.com"

    def search_input(self,sk):
        self.by_id("kw").send_keys(sk)
    def search_button(self):
        self.by_id("su").click()
