from work.Shared.Open import Open
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import logging
import allure

class Welcome():

    def WelcomePage():
        WebDriverWait(Open.driver, 5).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.ocard:id/NewContent"]/android.widget.RelativeLayout/android.view.View'))) #5秒內看到開始那頁的logo
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:go welcome page success", allure.attachment_type.PNG)
        return
    
    def ChoseStartUsing():
        StartUsing = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Start')))
        StartUsing.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:see chose login success", allure.attachment_type.PNG)

    def ChosePhoneLogin():
        PhoneBtn = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Login')))
        PhoneBtn.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:see phone login page success", allure.attachment_type.PNG)

    def InputErrorNumber():
        InputField = WebDriverWait(Open.driver, 3).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Number')))
        #InputField.click()
        InputField.clear()
        InputField.send_keys('0800000000')
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:input phone number", allure.attachment_type.PNG)
        Verify = Open.driver.find_element(AppiumBy.ID, 'com.ocard:id/Verify')
        Verify.click()
        ErrorMessage = WebDriverWait(Open.driver, 5).until(EC.visibility_of_element_located((AppiumBy.ID, 'com.ocard:id/Message'))) 
        if ErrorMessage.text == "即將發送簡訊認證碼至以上手機號碼，請確認您輸入的手機號碼正確無誤":
            logging.info("Error message success, is: "+ErrorMessage.text)
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:有出現錯誤訊息並且正確", allure.attachment_type.PNG)
        else:
            logging.info("Error Message fail")
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:錯誤訊息失敗", allure.attachment_type.PNG)
        choseErrorMessageConfirm = Open.driver.find_element(AppiumBy.ID, 'com.ocard:id/Confirm')
        choseErrorMessageConfirm.click()
        ChangPhoneNumber = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Previous')))
        ChangPhoneNumber.click()
        InputField.clear()


    def InputSuccessNumber():
        InputField = WebDriverWait(Open.driver, 3).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Number')))
        #InputField.click()
        InputField.clear()
        InputField.send_keys('輸入你的電話號碼') #請在這邊改為自己的電話
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:input phone number", allure.attachment_type.PNG)
        Verify = Open.driver.find_element(AppiumBy.ID, 'com.ocard:id/Verify')
        Verify.click()
        Confirm = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Confirm')))
        Confirm.click()
        sleep(5)
        
    def photoPermissionsDontAllow():
        sleep(5)
        photoPermissions = WebDriverWait(Open.driver, 60).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.ocard:id/NotificationLayout"])[1]')))
        photoPermissions.click()
        DontAllow = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')))
        DontAllow.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:拒絕相機權限", allure.attachment_type.PNG)

    def LocationPermissionsDontAllow():
        LocationPermiss = WebDriverWait(Open.driver, 60).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.ocard:id/NotificationLayout"])[2]')))
        LocationPermiss.click()
        DontAllow = WebDriverWait(Open.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')))
        DontAllow.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:拒絕位置權限", allure.attachment_type.PNG)

    def MobileSpacePermissionsDontAllow():
        MobileSpacePermiss = WebDriverWait(Open.driver, 60).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.ocard:id/NotificationLayout"])[3]')))
        MobileSpacePermiss.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:拒絕手機空間權限", allure.attachment_type.PNG)

class Home():

    def SeeHomePage():
        WebDriverWait(Open.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ocard:id/RecyclerView"])[1]/androidx.recyclerview.widget.RecyclerView')))
        return
    allure.attach(Open.driver.get_screenshot_as_png(), "截圖:首頁", allure.attachment_type.PNG)
    
    def SlideBanner():
        sleep(5)
        Open.driver.swipe(1400,530,55,530, 500) #滑動Banner
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:在首頁滑動到右側搜尋", allure.attachment_type.PNG)
    
    def ChoseBanner():
        Banner = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.ocard:id/exo_subtitles"]/android.view.View')))
        Banner.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:選擇上面橫幅", allure.attachment_type.PNG)
        
    def BackBannerAndGoHome():
        BackBtn = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Back')))
        BackBtn.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:從橫幅回到首頁", allure.attachment_type.PNG)

    def explore():
        explore = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="探索"]')))
        explore.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:點擊探索", allure.attachment_type.PNG)

    def Ocoin():
        Ocoin = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Ocoin"]')))
        Ocoin.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:點擊Ocoin", allure.attachment_type.PNG)
        try:
            OcoinConfirm = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Confirm')))
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:Ocoin權限確認", allure.attachment_type.PNG)
            OcoinConfirm.click()
        except:
            pass


    def Scanning():
        Scanning = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="掃碼"]')))
        Scanning.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:點擊掃描", allure.attachment_type.PNG)
        try:
            ScanningConfirm = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Confirm')))
            ScanningConfirm.click()
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:掃描權限1", allure.attachment_type.PNG)
            ScanningDoneAllow = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button')))
            ScanningDoneAllow.click()
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:掃描權限2", allure.attachment_type.PNG)
            ScanningCancel = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.ocard:id/Cancel')))
            ScanningCancel.click()
            allure.attach(Open.driver.get_screenshot_as_png(), "截圖:掃描權限3", allure.attachment_type.PNG)
        except:
            pass

    def MemberCard():
        MemberCard = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="會員卡"]')))
        MemberCard.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:點擊會員卡", allure.attachment_type.PNG)

    def MyInfo():
        MyInfo = WebDriverWait(Open.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="我的"]')))
        MyInfo.click()
        allure.attach(Open.driver.get_screenshot_as_png(), "截圖:點擊我的", allure.attachment_type.PNG)
