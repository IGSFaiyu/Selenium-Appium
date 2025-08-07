from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

# 配置手机参数（替换成你的设备信息）
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R9WW30AL79T"  # 执行 `adb devices` 获取
options.automation_name = "UiAutomator2"
# options.browser_name = "Chrome"  # 使用 Chrome 浏览器
# options.chromedriver_executable = "C:\\project\\Selenium\\test\\chromedriver-win64\\chromedriver.exe"
# options.app_package = "com.facebook.katana"
# options.app_activity = "com.facebook.katana.LoginActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# try:
    # 切换到 WEBVIEW 上下文
    # webview_context = driver.contexts[1]  # 通常是第二个上下文
    # driver.switch_to.context(webview_context)

    # # 现在可以使用 Selenium 的 Web 定位方式
    # driver.get("https://www.google.com")

    # # 示例：点击搜索框（使用 CSS_SELECTOR）
    # # search_box = WebDriverWait(driver, 10).until(
    # #     EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='q']"))
    # # )
    # # search_box.send_keys("Hello Appium")
time.sleep(15)
# search_box = driver.find_element(AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.facebook.katana:id/(name removed)"])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
# search_box.click()
# search_input = driver.find_element(AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.facebook.katana:id/(name removed)"])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
# search_input.send_keys("Hello Appium")
# el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(7)")
# el14.click()
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(901, 545)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
driver.save_screenshot("screenshots/Welfare and Education/android/test.png")

# el15 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(0)")
el15.send_keys("123")
driver.save_screenshot("current_screen.png")
print("start")

# finally:
driver.quit()  # 关闭会话