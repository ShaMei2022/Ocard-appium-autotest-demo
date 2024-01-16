這是一份關於 **Ocard APP** 自動化當中，所使用的方式、工具的介紹。

---
## 所需先安裝的工具、套件及介紹
1 **python3**:
我使用的語言是python 3代以上的版本，這是最主要程式語言，優先下載
2. **pytest**:
使用的測試框架
3. **pytest-bdd**:
所使用的行為驅動開發
4. **allure-pytest**:
產出報表的工具， 生成報表: pytest --alluredir=./test_report ； 讀取報表: allure serve ./test_report
5. **Appium、Selenium3.14版**:
網頁測試的框架
6. **Appium Python Client**:
Pyhton驅動Appium的工具