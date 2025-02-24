


from selenium import webdriver
from selenium.webdriver.common.by import By


'''
with webdriver.Chrome() as driver: 
    driver.get('https://www.naver.com')
'''


driver = webdriver.Chrome() # 실행 브라우저
driver.get('https://news.naver.com')
driver.quit()


xpath = '/html/body/img'
e = driver.find_element(By.XPATH,xpath)
print(e.text)