import logging
from setting import ios_setting
from appium import webdriver
import allure
import warnings
warnings.simplefilter("ignore")


class Open():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',desired_capabilities=ios_setting.desired_caps)

    def openAPP():
        dr = Open().driver
        logging.info('開啟手機模擬器:[IOS]')
        allure.attach(dr.get_screenshot_as_png(), '截圖:開啟手機模擬器:[IOS]', allure.attachment_type.PNG)
        return dr.delete_all_cookies()
    
class Close():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',desired_capabilities=ios_setting.desired_caps)
    
    def closeApp():
        dr = Open().driver
        return dr.quit()