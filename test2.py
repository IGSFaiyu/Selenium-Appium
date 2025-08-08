import sys
sys.path.append("./")
import test_command
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

options = UiAutomator2Options()
options.platform_name='Android'
options.automation_name='uiautomator2'
options.device_nme='R9WW30AL79T'
# options.app_package='com.android.settings'
# options.app_activity='.Settings'
options.language='en'
options.locale='US'

# options.app_package = "com.facebook.katana"
# options.app_activity = "com.facebook.katana.LoginActivity"

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=options)

check_region = (770, 1022, 240, 240)  # (x, y, width, height)
template_image = "skill1.png"

# 执行检查
# is_match, confidence, position = command.check_image_match(
#     driver,
#     template_image,
#     check_region,
#     threshold=0.85,
#     save_debug=True
# )

# if is_match:
#     print(f"匹配成功！置信度: {confidence:.2f}, 位置: {position}")
#     # 可以点击匹配到的位置
#     tap_x = position[0] + 25  # 点击中心点
#     tap_y = position[1] + 25
#     driver.tap([(tap_x, tap_y)])
# else:
#     print("未找到匹配图片")
    
    
region_image = test_command.capture_region(driver, 200, 1022, 240, 240, "skill7.png")
# nounal skill
# skill 1: 70, 1022, 240, 240
# skill 2: 420, 1022, 240, 240
# skill 3: 770, 1022, 240, 240

#spuer skill
# skill 1: 200, 1022, 240, 240
# skill 2: 650, 1022, 240, 240

print('end')