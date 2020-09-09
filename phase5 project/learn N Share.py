from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\Dell\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:/Users/Dell/Desktop/Github%20file/Project-PhaseIV/index.html')

button = driver.find_element_by_xpath('//button[@class="btn btn-info my-2"]')
button.click()

button1 = driver.find_element_by_xpath('//button[@value="1"]')
button1.click()
header1 = driver.find_elements_by_tag_name('tr')
for i in range(0,6):
    print(header1[i].text)

button2 = driver.find_element_by_xpath('//button[@value="2"]')
button2.click()
header2 = driver.find_elements_by_tag_name('tr')
for i in range(0,6):
    print(header2[i].text)

button3 = driver.find_element_by_xpath('//button[@value="3"]')
button3.click()
header3 = driver.find_elements_by_tag_name('tr')
for i in range(0,6):
    print(header3[i].text)

button4 = driver.find_element_by_xpath('//button[@value="4"]')
button4.click()
header4 = driver.find_elements_by_tag_name('tr')
for i in range(0,6):
    print(header4[i].text)
