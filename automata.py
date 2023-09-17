from selenium import webdriver
import time

web=webdriver.Chrome()
web.get('https://forms.gle/VmroKJ4BNBvroE3n7')
web.maximize_window()
time.sleep(3)

sname='ROHAN'
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)

mobile='9487717218'
phone=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone.send_keys(mobile)

sel_button=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')
sel_button.click()

col_name="Kingston Engineering College"
cname=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
cname.send_keys(col_name)

