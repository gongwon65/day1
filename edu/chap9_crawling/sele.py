


from selenium import webdriver
from selenium.webdriver.common.by import By



with webdriver.Chrome() as driver: 
    driver.get('https://www.naver.com')
    e_list = driver.find_elements(By.TAG_NAME,'p')
    for e in e_list:
        print(e.text)

'''
driver = webdriver.Chrome() # 실행 브라우저
driver.get('https://www.naver.com')
driver.quit()
'''

'''
e = driver.find_element(By.TAG_NAME,'div') \
.find_element(By.TAG_NAME, 'p')
print(e.text)
'''

'''
e_list = driver.find_elements(By.TAG_NAME,'p')
for e in e_list:
    print(e.text)
'''

'''
xpath = '/html/body/img'
e = driver.find_element(By.XPATH,xpath)
print(e.text)
'''