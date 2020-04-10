from selenium import webdriver
from time import sleep
from DeleteYTCommentsBot import DeleteYTCommentsBot
from KillComments import  KillComments

class Google:
    def __init__(self, username, password):
        # chrome_options = webdriver.ChromeOptions(); # uncomment out these lines if Chrome flags are an issue
        # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        self.driver = webdriver.Chrome('PATH NAME')  # REPLACE PATH NAME: example /Users/OS_user/Developer/chromedriver
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        sleep(3)
        DeleteYTCommentsBot(self.driver)
        # self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        # self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        # sleep(3) #this did not work, so username is handled in DeleteYTCommentsBot.py
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://www.youtube.com/feed/history/comment_history')
        sleep(5)
        KillComments(self.driver)

