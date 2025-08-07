from appium import webdriver as appium_webdriver
from selenium  import webdriver as selenium_webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv(".env.windows")


options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R9WW30AL79T"  # 执行 `adb devices` 获取
options.automation_name = "UiAutomator2"
# options.browser_name = "Chrome"  # 使用 Chrome 浏览器
# options.chromedriver_executable = "C:\\project\\Selenium\\test\\chromedriver-win64\\chromedriver.exe"
# options.app_package = "com.facebook.katana"
# options.app_activity = "com.facebook.katana.LoginActivity"

driver = appium_webdriver.Remote("http://127.0.0.1:4723", options=options)
    

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# open Chrome
# el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
# el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/search_box_text")
el2.send_keys("https://www.crossboundaryservices.gov.hk/en/hk_service/index.html")
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.android.chrome:id/line_1\").instance(0)")
el3.click()
driver.save_screenshot("screenshots/Welfare and Education/android/test.png")
driver.quit()  # 关闭会话