from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="./chromedriver")
# 2. Mở thử một trang web
browser.get("http://xemdiem.utc2.edu.vn/")

# 2.1 dien thong tin vao o
# txtUser = browser.find_element_by_id("MA_SINHVIEN")
# txtUser.send_keys(5951030057)
click1 = browser.find_element_by_xpath(
    "/html/body/form/table/tbody/tr[2]/td/p/table/tbody/tr[1]/td/div/table/tbody/tr[1]/td[2]/input[2]")
click1.click()
inputid = browser.find_element_by_id("dangky1_TextBox1")
inputid.send_keys("5951030057")
secarh = browser.find_element_by_id("Tim")
secarh.click()
click2 = browser.find_element_by_id("aaaaaaakkkkkk")
click2.click()
find = browser.find_element_by_xpath(
    "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/p[2]/table/tbody/tr/td/table/tbody")
print(find.text)
f = open("test.txt", "w")


f.write(find.text)

value = browser.find_element_by_xpath(
    "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/p[2]/font/table/tbody/tr[1]/td[2]/font/strong")
print("diem", value.text)
f.write(value.text)
browser.close()
# #matkhau
# txtMk = browser.find_element_by_id("MAT_KHAU")
# txtMk.send_keys("taminh13")
# #capcha
# capcha = browser.find_element_by_id("MaAnToan")
# capcha.send_keys(input("NHap ma an toan:  "))
# #login
# capcha.send_keys(Keys.ENTER)
# sleep(5)
# linka = browser.find_element_by_xpath ("/html/body/div[1]/div/div/div[3]/ul/li/a")
# linka.click()
# sleep(2)
# linka2 = browser.find_element_by_xpath ("/html/body/div[1]/div/div/div[3]/ul/li/ul/li[3]/a")
# linka2.click()
