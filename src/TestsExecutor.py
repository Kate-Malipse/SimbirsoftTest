import Tests
from selenium import webdriver
import sys

if __name__ == "__main__":
    args = sys.argv
    
    is_debug = len(args) > 1 and args[1] == 'DEBUG'

    #Local driver
    if is_debug:
        driver = webdriver.Firefox()
    #Grid Remote: send arguments to Hub
    else:
        node_port = args[1]
        browser_name = args[2]
        platform_name = args[3]
        
        driver = webdriver.Remote(
            command_executor = "http://localhost:5000/wd/hub",
            desired_capabilities = { "browserName": browser_name, "platform": platform_name, "node": node_port }
        )

#Tests List
Tests.test_send_new_mail_yandex(driver)
Tests.test_send_new_mail_google(driver)
