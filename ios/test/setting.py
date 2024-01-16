# -*- coding: utf-8 -*-
import os

TIMEOUT = os.getenv('TIMEOUT','300')

class ios_setting():
    desired_caps = {
        'xcodeOrgId': 'Conrad Test',
        'platformName': 'iOS',
        'platformVersion': '16.2',
        'automationName': 'XCUITest',
        'deviceName': 'iPhone 14 Pro Max', 
        'app': '/Users/Conrad/Downloads/app/Ocard.app',
        'bundleId': 'com.Conrad.Ocard.ios',
        # 'noReset': 'true', #這是在本地測試時，可以打開的，他將不會重新抓取APP
        # 'autoAcceptAlerts': 'true',  #自動接受所有權限彈出的視窗
        # 'autoDismissAlerts': 'ture', #自動關閉所有權限彈出的視窗
    }
    