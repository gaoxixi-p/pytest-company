from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# 全屏
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(2)
#百度首页查询热榜第一，并关闭当前网页
driver.find_element_by_xpath("//a[@class='title-content c-link c-font-medium c-line-clamp1']/span[1]").click()
driver.back()
url =driver.current_url
print(url)
#百度首页输入框输入内容，点击查询
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("pyton")
# driver.find_element_by_xpath("//input[@type='submit']").click()


sleep(2)
#driver.quit()
