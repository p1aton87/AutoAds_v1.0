from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AutoSellerReg:
    def __init__(self, eml, pas):
        driver = webdriver.Firefox()
        self.driver = driver
        self.start_page()
        self.reg_menu()
        self.login_menu()
        self.input_login(emails=eml, passwrd=pas)

    def start_page(self):
        self.driver.get('https://m.leboard.ru/')

    def reg_menu(self):
        entry = self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/a/span')
        entry.click()

    def login_menu(self):
        login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/a')
        login.click()

    def input_login(self, emails, passwrd):
        email = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[1]/input')
        email.click()
        email.send_keys(emails)
        password = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[2]/div/input')
        password.click()
        password.send_keys(passwrd)
        send_empass = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[3]/input')
        send_empass.click()


class AutoSellerControl:

    def __init__(self, email, password):
        try:
            self.ASR = AutoSellerReg(email, password)
            self.include_all()
            sleep(14.0)
            self.ASR.driver.close()
            sleep(1)
            self.ASR.driver.quit()
        except Exception:
            self.ASR.driver.close()
            sleep(1)
            self.ASR.driver.quit()

    def menu(self):
        my_menu = self.ASR.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/span')
        my_menu.click()

    def my_ads(self):
        myads = self.ASR.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/ul/li[3]/a')
        myads.click()

    def up_ads(self):
        up_ads = self.ASR.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[2]/div[4]/div[1]/article/div[2]/a')
        up_ads.click()

    def submit_up_ads(self):
        sub_up = self.ASR.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[1]/div[2]/a[1]')
        sub_up.click()

    def include_all(self):
        self.menu()
        self.my_ads()
        self.up_ads()
        self.submit_up_ads()

