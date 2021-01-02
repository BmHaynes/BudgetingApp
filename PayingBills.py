import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import PassUsers

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def pay_internet():
    driver.get(
        "https://authorize.suddenlink.net/saml/module.php/authSynacor/login.php?AuthState=_bf3a0d9cf8458c3d7048bd97804558210f3190c6be%3Ahttps%3A%2F%2Fauthorize.suddenlink.net%2Fsaml%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Daccount.suddenlink.net%26cookieTime%3D1608688025%26allowCreate%3D0")
    login = driver.find_element_by_css_selector("input#username")
    login.send_keys(PassUsers.suddenlinuser)
    password = driver.find_element_by_css_selector("input#password")
    password.send_keys(PassUsers.suddenlinkpass, Keys.ENTER)
    driver.get("https://account.suddenlink.net/my-account/mybill/payment.html")
    time.sleep(10)
    pastdue = driver.find_element_by_css_selector("input#pastDueBalance")
    pastdue.click()
    pastdue.send_keys(Keys.ENTER)
    time.sleep(10)
    select_payment = driver.find_element_by_css_selector("input")
    select_payment.click()
    select_payment.send_keys(Keys.ENTER)


def pay_verizon():
    driver.get("https://secure.verizon.com/vzauth/UI/Login")
    time.sleep(5)
    login = driver.find_element_by_name("IDToken1")
    login.send_keys(PassUsers.verizonuser, Keys.TAB, PassUsers.verizonpass)
    time.sleep(1)
    login.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get("https://myvpostpay.verizon.com/ui/bill/secure/pb?adobe_mc=MCMID%3D69040805911136477303219029360190440353%7CMCORGID%3D843F02BE53271A1A0A490D4C%2540AdobeOrg%7CTS%3D1608809236&mboxSession=0eb0f9474d13400290e1123e3501c346#/")


def pay_electric():
    driver.get("https://www.myentergy.com/s/login/")
    time.sleep(5)
    login = driver.find_element_by_css_selector("lightning-input#input-0.slds-form-input")
    login.send_keys(Keys.TAB, PassUsers.entergyuser, Keys.TAB, PassUsers.entergypass)
    time.sleep()
    login.send_keys(Keys.ENTER)


def pay_water():
    driver.get("https://www.diversifiedbillpay.com/v1/login/login-standard.php?company=MAGNOLIAMWS")
    pay = driver.find_element_by_id("continueButton")
    pay.click()
    time.sleep(10)
    login = driver.find_element_by_name("username")
    login.click()
    login.send_keys(PassUsers.wateruser, Keys.TAB, PassUsers.waterpass)
    time.sleep(1)
    login.send_keys(Keys.ENTER)



def pay_gas():
    pass

def pay_house():
    pass

def pay_B_cap_one():
    pass




# pay_internet()
# pay_electric()
pay_verizon()
# pay_water()
# driver.close()
