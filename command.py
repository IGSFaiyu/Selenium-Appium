
import io
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from io import BytesIO
from PIL import Image
from pathlib import Path
import base64

class CommandClass:
    def __init__(self, envFile=".env.windows", screenshotsPath="screenshots"):
        self.envFile = envFile
        load_dotenv(self.envFile)
        
        self.driver = None
        self.driver2 = None
        self.platformName = None
        self.webdriverBy = None
        self.screenshotsPath = screenshotsPath
        self.screenshotsIndex = 0
        self.platform_name = os.getenv("platform_name")
        
        if self.platform_name.lower() == "android":
            # Android 配置
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = os.getenv("device_name")
            options.browser_name = "Chrome"
            options.automation_name = "UiAutomator2"
            options.chromedriver_executable = os.getenv("chromedriver_executable")
            options.chrome_options = {
                "args": [
                    "--disable-infobars",
                    "--hide-scrollbars",
                    "--disable-notifications",
                ]
            }
            self.driver = appium_webdriver.Remote("http://127.0.0.1:4723", options=options)
            
            # 切换到 WEBVIEW 上下文
            webview_context = self.driver.contexts[1]
            service = Service(executable_path=os.getenv("chromedriver_executable"))
            self.driver.switch_to.context(webview_context)
            self.platformName = "android"
            self.webdriverBy = AppiumBy
            
        
        elif self.platform_name.lower() == "windows":
            options = Options()
            service = Service(os.getenv("chromedriver_executable"))
            options.add_argument("user-data-dir={0}".format(os.getenv("chrome_profile"))) #Path to your chrome profile
            options.add_argument("profile-directory={0}".format(os.getenv("profile_name"))) #Path to your chrome profile
            options.add_argument('--remote-debugging-pipe')
            options.add_argument('--enable-chrome-browser-cloud-management')
            options.add_experimental_option("detach", True)
            options.binary_location = os.getenv("chrome")
            options.page_load_strategy = 'none'
            self.driver = selenium_webdriver.Chrome(service=service,options=options)
            self.platformName = "windows"
            self.webdriverBy = By
        
        else:
            raise ValueError(f"不支持的平台: {self.platform_name}")
        self.screenshotsPath += f"/{self.platformName}"
        Path(self.screenshotsPath).mkdir(parents=True, exist_ok=True)
        
    def goPage(self, url):
        self.driver.get(url)
        
    def inputElem(self, type, selectorTxt, content):
        by_method = getattr(self.webdriverBy, type)
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, selectorTxt))
        )
        elem.send_keys(content)
        
    def clickElem(self, type, selectorTxt):
        if self.platform_name.lower() == "android":
            self.driver.execute_script("document.activeElement.blur();")
        by_method = getattr(self.webdriverBy, type)
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, selectorTxt))
        )
        elem.click()
        
    def uploadFile(self, type, selectorTxt, content):
        by_method = getattr(self.webdriverBy, type)
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, selectorTxt))
        )
        if(self.platform_name.lower() == "android"):
            with open(content, "rb") as image_file:
                image_base64  = base64.b64encode(image_file.read()).decode("utf-8")
                
            self.driver.push_file('/data/local/tmp/test.png', image_base64)
            elem.send_keys('//data//local//tmp//test.png')
        else:
            elem.send_keys(os.path.abspath(content))
        
    def android_capture_region(self, x=None, y=None, width=None, height=None):
        self.screenshotsIndex += 1
        filePath = self.screenshotsPath + "/" + str(self.screenshotsIndex) + ".png"
        self.driver.execute_script("document.activeElement.blur();")
        # self.driver.get_screenshot_as_file(filePath)
        
        driver = self.driver
        # Android 配置
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = os.getenv("device_name")
        options.automation_name = "UiAutomator2"
        self.driver = appium_webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.save_screenshot(filePath)
        
        self.driver = driver
        # viewport_bytes = self.driver.get_screenshot_as_png()
        # viewport_screenshot = Image.open(BytesIO(viewport_bytes))
        # viewport_width = viewport_screenshot.width
        # viewport_height = viewport_screenshot.height
        # web_viewport_height = self.driver.execute_script("return window.innerHeight")
        # gap_height = viewport_height / web_viewport_height
        
        # total_height = round(self.driver.execute_script("return document.body.scrollHeight") * gap_height)
        # viewport_height = self.driver.execute_script("return window.innerHeight") * gap_height
        # full_screenshot = Image.new("RGB", (viewport_width, total_height))
        # current_position = 0
        # while current_position < total_height:
        #     self.driver.execute_script(f"window.scrollTo(0, {current_position})")
        #     screenshot_bytes = self.driver.get_screenshot_as_png()
        #     screenshot = Image.open(BytesIO(screenshot_bytes))
        #     y_position = current_position if current_position + viewport_height <= total_height else total_height - viewport_height
        #     full_screenshot.paste(screenshot, (0, int(y_position)))
        #     full_screenshot.save(filePath)
        #     current_position += viewport_height

        # full_screenshot.save(filePath)
        
        
    def capture_region(self, x=None, y=None, width=None, height=None):
        time.sleep(0.5)
        
        if self.platform_name.lower() == "android":
            self.android_capture_region(x, y, width, height)
            return
        
        self.screenshotsIndex += 1
        filePath = self.screenshotsPath + "/" + str(self.screenshotsIndex) + ".png"
        
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        viewport_height = self.driver.execute_script("return window.innerHeight")
        full_screenshot = Image.new("RGB", (self.driver.get_window_size()["width"], total_height))
        current_position = 0
        while current_position < total_height:
            self.driver.execute_script(f"window.scrollTo(0, {current_position})")
            screenshot_bytes = self.driver.get_screenshot_as_png()
            screenshot = Image.open(BytesIO(screenshot_bytes))
            y_position = current_position if current_position + viewport_height <= total_height else total_height - viewport_height
            full_screenshot.paste(screenshot, (0, y_position))
            current_position += viewport_height

        full_screenshot.save(filePath)
        
    def waitForPageLoad(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
    def waitForElemLoad(self, type, selectorTxt, timeout=30):
        by_method = getattr(self.webdriverBy, type)
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by_method, selectorTxt))
        )
        
    def switchTab(self, index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[index])
        
    def quit(self):
        self.driver.quit()