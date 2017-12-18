import time
# Stale means the element no longer appears on the DOM of the page
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver

def wait_for_load(a_driver):
    element = a_driver.find_element_by_tag_name('html')
    print('content', element)
    count = 0
    while True:
        count += 1
        # 超过10s，直接返回
        if count > 20:
            print('Timing out after 10s and returning')
            return

        time.sleep(0.5)  # 检查还是不是同一个element，如果不是，说明这个html标签已经不再DOM中了。如果不是抛出异常
        new = a_driver.find_element_by_tag_name('html')
        print('new', new)
        if element != new:
            raise StaleElementReferenceException('刚才重定向了！')

driver = webdriver.PhantomJS(executable_path="E:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get('https://pythonscraping.com/pages/javascript/redirectDemo1.html')
try:
    wait_for_load(driver)
except StaleElementReferenceException as e:
    print(e.msg)
finally:
    print(driver.page_source)
    driver.close()