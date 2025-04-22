import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 代理
# res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
# proxy_string = res.json()['data']['proxy_list'][0]
# print(f"获取代理：{proxy_string}")

service = Service("chromedriver.exe")
opt = webdriver.ChromeOptions()

# opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false') # 不加载图片

opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=opt)

driver.implicitly_wait(10)

with open('hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})


driver.get('https://www.jd.com/')
tag = driver.find_element(
    By.XPATH,
    '//*[@id="key"]'
)
tag.send_keys("iphone手机")


tag = driver.find_element(
    By.XPATH,
    '//*[@id="search"]/div/div[2]/button'
)
tag.click()

tag_list = driver.find_elements(
    By.XPATH,
    '//*[@id="J_goodsList"]/ul/li'
)
for tag in tag_list:
    # title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]//em').text
    title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]/a/em').text
    print(title)
driver.close()