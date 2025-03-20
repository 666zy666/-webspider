from selenium import webdriver #用于操作浏览器
from  selenium.webdriver.chrome.options import Options#用于设置浏览器
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #元素定位
import time
import requests
import ddddocr
def find_element_TagName(name,n):
    #标签名查找
    result = a1.find_elements(By.TAG_NAME,name)[n]
    return result
def click_element(element):
    #点击元素
    element.click()
def screennshot_():
    #浏览器截图
    a1.get_screenshot_as_file()#文件存储地址，格式尽量用png
def set():
    q1 = Options()
    # 增加兼容性
    # q1.add_argument('--no-sandbox')
    q1.add_experimental_option('detach', True)
    # 创建并启动浏览器
    a1 = webdriver.Chrome(options=q1, service=Service('../图片验证码/chromedriver.exe'))
    return a1

def send_keys(element,m):
    #搜索框输入
    element.send_keys()
def find_element_Xpath(value):
        # 普通xpath定位（属性+路径）
        # 如过属性随机的（用完整路径定位）
        result = a1.find_element(By.XPATH, value)
        return result
if __name__ =="__main__":
    a1 = set()
    a1.get('https://study.gzgsmooc.org.cn/login?path=%2Fhome')
    result = find_element_TagName('input',1)
    time.sleep(1)
    result.send_keys('202202250140')
    time.sleep(1)
    result = find_element_TagName('input', 2)
    time.sleep(1)
    result.send_keys('GZgs@281819' )
    time.sleep(1)
    dict =find_element_Xpath('/html/body/div[3]/div/div/div[3]/div[1]/div/div[2]/form/div[3]/div/div/span[2]/span/div/img').screenshot_as_base64
    ocr = ddddocr.DdddOcr(show_ad=False)
    code = ocr.classification(dict)
    print(code)
    #登录
    result = find_element_Xpath('//*[@id="__layout"]/div/div[3]/div[1]/div/div[2]/form/div[3]/div/div/input')
    result.send_keys(code)
    time.sleep(2)
    result =find_element_Xpath('/html/body/div[3]/div/div/div[3]/div[1]/div/div[2]/form/div[4]/div/button')
    click_element(result)
    time.sleep(15)
    a1.close()