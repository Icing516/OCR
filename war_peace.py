#coding:utf-8

import time
from urllib import  urlretrieve
import subprocess
from selenium import webdriver

# driver =webdriver.PhantomJS(executable_path='D:\python\phantomjs')
driver =webdriver.Chrome()

driver.get('https://www.amazon.com/War-Peace-Vintage-Classics-Tolstoy/dp/1400079985/ref=oosr')
driver.maximize_window()
time.sleep(2)

driver.find_element_by_id('imgBlkFront').click()
imageList = set()

time.sleep(3)
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
# 获取已加载的新页面（一次可以加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
driver.quit()
# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"],
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
