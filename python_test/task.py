# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:19:27 2020

@author: AbdullahZezo
"""
from seleniumwire import webdriver 
import unittest
import time  
from selenium.webdriver.common.keys import Keys  

class Test(unittest.TestCase):
    
    def setUp(self) :
        #Create new Chrome Session
        self.driver = webdriver.Chrome(r"C:\Users\AbdullahZezo\Desktop\chromedriver.exe")
        self.driver.maximize_window()
        
        self.addCleanup(self.take_screenshots)
        self.driver.implicitly_wait(5)
        
        
        
    def take_screenshots(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")
                self.driver.quit()
        
        

    def get_status(self) :
        # Access requests via the `requests` attribute
        for request in self.driver.requests:
            if request.response:
                if 'sasCache' in request.path:
                    print(
                        request.path,
                        request.response.status_code,
                        request.response.headers,
                        request.body,
                        '\n'
                    )
                    
    def test_a_register(self) :
        #Navigate to app page
        self.driver.get("https://www.phptravels.net/register")
        
        self.get_status()
        
        self.driver.find_element_by_name("firstname").send_keys("Abdullah")
        self.driver.find_element_by_name("lastname").send_keys("Abdelaziz")
        self.driver.find_element_by_name("phone").send_keys("01226302807")
        self.driver.find_element_by_name("email").send_keys("abdullahabdelaziz0@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Aa010012")
        self.driver.find_element_by_name("confirmpassword").send_keys("Aa010012")
        self.driver.find_element_by_class_name("signupbtn.btn_full.btn.btn-success.btn-block.btn-lg").send_keys(Keys.ENTER)
        time.sleep(3)
        
        url = self.getCurrentUrl()
        self.assertUrl(url)
                
    
    
    def test_b_login_1(self) :
        self.driver.get("https://www.phptravels.net/login")
        
        self.get_status()
    
        self.driver.find_element_by_name("username").send_keys("abdullahabdelaziz0@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Aa010012")
        self.driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn").send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        url = self.getCurrentUrl()
        self.assertUrl(url)
        
    def test_b_login_2(self) :
        self.driver.get("https://www.phptravels.net/login")
        
        self.get_status()
    
        self.driver.find_element_by_name("username").send_keys("abdullahabdelaziz0@gmail.com")
        self.driver.find_element_by_name("password").send_keys("12345678")
        self.driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn").send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        url = self.getCurrentUrl()
        self.assertUrl(url)
        
    def test_b_login_3(self) :
        self.driver.get("https://www.phptravels.net/login")
        
        self.get_status()
    
        self.driver.find_element_by_name("username").send_keys("abdullahabdelaziz0@gmail.com")
        self.driver.find_element_by_name("password").send_keys("asdfghjk")
        self.driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn").send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        url = self.getCurrentUrl()
        self.assertUrl(url)
        
    def test_b_login_4(self) :
        self.driver.get("https://www.phptravels.net/login")
        
        self.get_status()
    
        self.driver.find_element_by_name("username").send_keys("abdullahabdelaziz@gmail.com")
        self.driver.find_element_by_name("password").send_keys("Aa010012")
        self.driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn").send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        url = self.getCurrentUrl()
        self.assertUrl(url)

    def getCurrentUrl(self) :
        url = self.driver.current_url()
        return url
    
    def assertUrl(self, actual_url) :
        expected_url = "https://www.phptravels.net/account/"
        self.assertEqual(expected_url, actual_url)


    def tearDown(self):
            self.driver.quit()
    
    
    
            
if __name__ == '__main__' :
    unittest.main()
        
