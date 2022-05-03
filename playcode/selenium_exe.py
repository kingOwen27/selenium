import imp
from lib2to3.pgen2 import driver
from select import select
from time import monotonic, sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com")
# driver.get("https://www.126.com")
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('上海海事大学')
# driver.set_window_size(800,600)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')
# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys('selenium')
# driver.find_elements_by_css_selector(".s_ipt").send_keys('selenium')

# driver.find_element(By.ID,'kw').send_keys('selenium')
# driver.find_element_by_id('su').submit()
# driver.save_screenshot("baidu.png")
# js="window.scrollTo(100,450);"
# text="hello world"
# js="document.getElementById('id').value='"+ text +"';"
# driver.execute_script(js)

# text=driver.find_element_by_id('cp').text
# print(text)
# l=driver.find_element_by_xpath("//input[@id='kw']").size
# print(l)

# driver.set_window_size(480,800)
# driver.get("https://blog.csdn.net/weixin_41635750/article/details/117536676")
# driver.back()
# sleep(1)
# driver.forward()
# driver.refresh()

# tmp=driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(tmp).perform()
# driver.quit()

# driver.find_element_by_xpath("//input[@id='kw22']")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL,'a')
# sleep(1)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL,'x')
# driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL,'v')
# driver.find_element_by_id('su').submit()
# # driver.quit()
# print(driver.current_url)

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# element=WebDriverWait(driver,5,0.5).until(
#     EC.visibility_of_element_located((By.ID,"kw"))
# )
# element.send_keys('selenium')

# sleep(2)
# tmp=driver.find_elements_by_css_selector('iframe[id ^= "x-URS-iframe"]')
# # tmp=driver.find_element_by_xpath("//iframe[@id^='x-URS-iframe']")
# driver.switch_to.frame(tmp)
# driver.find_element_by_name("email").send_keys("1234")
# # sleep(1)
# driver.switch_to.default_content()

# se=driver.current_window_handle
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text('立即注册').click()
# driver.switch_to.window(se)

# from selenium.webdriver.support.select import Select
# driver.find_element_by_id('s-usersetting-top').click()
# driver.find_element_by_link_text('搜索设置').click()
# sleep(2)
# sel=driver.find_element_by_xpath("//select[@id='nr']")
# Select(sel).select_by_value('20')
# driver.find_element_by_class_name('prefpanelgo').click()
# al=driver.switch_to.alert
# sleep(1)
# al.accept()
# driver.quit()

# driver.get("https://pypi.org/project/selenium/#files")
# driver.find_element_by_partial_link_text("selenium-4.1.3-py3-none-any.whl ").click()

# opt =webdriver.ChromeOptions()
# opt.add_experimental_option('w3c',False)
# driver= webdriver.Chrome(chrome_options=opt)
# driver.get("https://www.jq22.com/yanshi4976")
# sleep(2)
# driver.switch_to.frame("iframe")
# driver.find_element_by_id("appDate").click()
# dw=driver.find_elements_by_class_name("dwwo")
# year=dw[0]
# action=webdriver.TouchActions(driver)
# action.scroll_from_element(year,0,10).perform()

# with open("info.txt","r") as tmp:
#     data=tmp.readlines()
# ans=[]
# for i in data:
#     u=i[:-1].split(":")
#     ans.append(u)
# print(ans)

# from xml.dom.minidom import parse
# dom=parse('config.xml')
# root=dom.documentElement
# tag=root.getElementsByTagName('platform')
# print(tag[0].firstChild.data)

