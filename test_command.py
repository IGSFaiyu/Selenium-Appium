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
    
def capture_region(driver, x, y, width, height, save_path=None):
    """
    捕获屏幕特定区域
    :param driver: Appium WebDriver
    :param x: 区域左上角x坐标
    :param y: 区域左上角y坐标
    :param width: 区域宽度
    :param height: 区域高度
    :param save_path: 保存路径(可选)
    :return: PIL.Image对象
    """
    # 获取整个屏幕截图
    screenshot_bytes = driver.get_screenshot_as_png()
    full_image = Image.open(BytesIO(screenshot_bytes))
    
    # 裁剪指定区域
    region = full_image.crop((x, y, x + width, y + height))
    
    if save_path:
        region.save(save_path)
    
    return region

def check_image_match(driver, template_path, region, threshold=0.8, save_debug=False):
    """
    检查屏幕指定区域是否匹配模板图片
    
    :param driver: Appium WebDriver实例
    :param template_path: 模板图片路径
    :param region: 要检查的区域 (x, y, width, height)
    :param threshold: 匹配阈值(0-1)
    :param save_debug: 是否保存调试图片
    :return: (是否匹配, 匹配度, 匹配位置)
    """
    # 1. 获取屏幕截图
    screenshot_bytes = driver.get_screenshot_as_png()
    screenshot = np.array(Image.open(BytesIO(screenshot_bytes)))
    
    # 2. 读取模板图片
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise ValueError(f"无法读取模板图片: {template_path}")
    
    # 3. 提取要检查的区域
    x, y, w, h = region
    region_img = screenshot[y:y+h, x:x+w]
    region_gray = cv2.cvtColor(region_img, cv2.COLOR_BGR2GRAY)
    
    # 4. 检查区域尺寸是否有效
    if region_gray.shape[0] < template.shape[0] or region_gray.shape[1] < template.shape[1]:
        return False, 0, None
    
    # 5. 执行模板匹配
    res = cv2.matchTemplate(region_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 6. 调试：保存匹配结果可视化
    if save_debug:
        debug_img = region_img.copy()
        if max_val >= threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
            cv2.rectangle(debug_img, top_left, bottom_right, (0, 255, 0), 2)
        cv2.imwrite("debug_match.png", debug_img)
    
    # 7. 返回结果
    match_pos = (x + max_loc[0], y + max_loc[1]) if max_val >= threshold else None
    return max_val >= threshold, float(max_val), match_pos
