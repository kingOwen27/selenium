from selenium import webdriver

ds = {'platform': 'ANY',
      'browserName': "chrome",
      'version': '',
      'javascriptEnabled': True
      }
dr = webdriver.Remote('http://192.168.101.7:4444/wd/hub', desired_capabilities=ds)
dr.get("https://www.baidu.com")
print(dr.name)


