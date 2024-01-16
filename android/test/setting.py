# -*- coding: utf-8 -*-
import os

class android_setting():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Pixel 6 Pro',
        'automationName': 'UiAutomator2', #Appium針對Android的驅動
        'avd': 'Pixel_6_Pro',    #本機執行的模擬器
        'app': 'C:/Coz/nweTest/Ocard.apk', #這是APP的位置
        #'noReset': 'true',          #這是在本地測試時，將不會重新抓取APP
        #'noReset': 'false',         #這是在CI測試時，需要重新抓取APP
        #'autoAcceptAlerts': 'true',     #自動接受所有權限彈出的視窗
    }
