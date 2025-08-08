from command import CommandClass

def main():
    print("Start")
    screenshotsPath = "screenshots/Welfare and Education"
    # command = CommandClass(".env.windows", screenshotsPath)
    # command = CommandClass(".env.emulator", screenshotsPath)
    command = CommandClass(".env.android", screenshotsPath)
    
    command.goPage("https://www.crossboundaryservices.gov.hk/en/hk_service/index.html")
    command.clickElem("LINK_TEXT", "Welfare and Education")
    command.clickElem("LINK_TEXT", "Application for Senior Citizen Card")
    command.waitForElemLoad("LINK_TEXT", "Eligibility Criteria")
    command.capture_region()
    command.clickElem("LINK_TEXT", "Submit Online Application")
    command.switchTab(1)
    command.capture_region()
    command.clickElem("XPATH", '//label[contains(., "I understand and agree to the")]//input')
    command.clickElem("LINK_TEXT", "Start Filling in a New Form")
    command.capture_region()
    command.clickElem("XPATH", '//label[contains(., "First Application")]//input')
    command.capture_region()
    command.clickElem("XPATH", '//button[contains(., "Next")]')
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#surname', "ff")
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#givenName', "ff")
    command.capture_region()
    command.clickElem("XPATH", '//label[contains(., "Male")]//input')
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#dobDay', "01")
    command.inputElem("CSS_SELECTOR", '#dobMonth', "01")
    command.inputElem("CSS_SELECTOR", '#dobYear', "1950")
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '[id="hkid.id"]', "T125876")
    command.inputElem("CSS_SELECTOR", '[id="hkid.checkDigit"]', "6")
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#typeOfAddress', "otherAddress")
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#otherAddress', "test")
    command.capture_region()
    command.inputElem("CSS_SELECTOR", '#tele', "12345678")
    command.clickElem("XPATH", '//label[contains(., "Same as above")]//input')
    command.capture_region()
    command.clickElem("CSS_SELECTOR", '#step2 #nextBtn')
    command.uploadFile("CSS_SELECTOR", '#photoFile', "screenshots/UploadFiles/1.png")
    command.uploadFile("CSS_SELECTOR", '#hkidCopyFile', "screenshots/UploadFiles/1.png")
    command.capture_region()
    command.clickElem("CSS_SELECTOR", '#step3 #nextBtn')
    command.capture_region()
    try:
        
        print("End")
    
    
    finally:
        command.quit()

if __name__ == "__main__":
    main()