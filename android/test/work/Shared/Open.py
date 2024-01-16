import logging
from setting import android_setting
from appium import webdriver
import allure


class Open():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',desired_capabilities=android_setting.desired_caps)   # 本機和mac使用的http url 使用的appium為2.x版
    
    def openAPP():
        dr = Open().driver
        logging.info('開啟手機模擬器:[Android]')
        allure.attach(dr.get_screenshot_as_png(), '截圖:開啟手機模擬器:[Android]', allure.attachment_type.PNG)

        return dr