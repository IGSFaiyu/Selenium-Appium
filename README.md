1. Download python https://www.python.org/downloads/
2. Download pip https://bootstrap.pypa.io/get-pip.py
3. cmd cd pip folder and run "python get-pip.py"
4. cmd run "pip install selenium appium-python-client pytest"
5. Download jdk https://www.oracle.com/java/technologies/downloads/?er=221886
6. Set environment path "JAVA_HOME"
7. Download Node.js https://nodejs.org/en/download
8. Download Appium cmd run "npm install -g appium"
9. Download ADB https://dl.google.com/android/repository/platform-tools-latest-windows.zip
10. Unzip and set environment path
11. Get android chrome version 
12. Download chromedriver https://storage.googleapis.com/chrome-for-testing-public/[android chrome version]/win64/chromedriver-win64.zip
13. Unzip chromedriver.zip
14. Get device name, cmd "adb devices"
15. Change .env.android device_name = [your device name] and chromedriver_executable = [your chromedriver.exe path]
15. Enable .env.android device_name
16. cmd "appium"
17. python welfareandEducation.py

Use docker:
1. Download python https://www.python.org/downloads/
2. Download docker https://docs.docker.com/desktop/setup/install/windows-install/
3. Download ADB https://dl.google.com/android/repository/platform-tools-latest-windows.zip
4. Unzip and set environment path
5. Show developer options "Settings > About phone > Software information" Tap "Build number" seven times
6. Open developer mode "Settings > Developer options" tap "On" button and USB-Debugging
7. Get device name, Cmd "adb devices" 
8. docker-compose up -d
9. cmd "adb shell ip route"
10. adb tcpip 5555
11. cmd "docker exec appium-container adb connect [ip route]:5555"
12. Change .env.android device_name to [ android device name] and chrome_version = [android chrome version]
13. Disable .env.android device_name
14. cmd "docker-compose --env-file .env.android up -d"
15. python welfareandEducation.py
