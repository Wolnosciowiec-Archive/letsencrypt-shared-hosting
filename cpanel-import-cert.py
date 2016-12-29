#-*- encoding: utf-8 -*-
import selenium.webdriver
import sys
import os
import time

class CpanelImportCert:

    def main(self):
        print(os.environ)
        self.browser = selenium.webdriver.Chrome()
        self.browser.get(os.environ['CPANEL_URL'])
        
        self.login()
        self.visit_ssl_manager()
        
    def login(self):
        
        self.browser.find_element_by_id('user').click()
        self.browser.find_element_by_id('user').send_keys(os.environ['USER'])

        self.browser.find_element_by_id('pass').click()
        self.browser.find_element_by_id('pass').send_keys(os.environ['PASSWORD'])
        
        self.browser.find_element_by_id('login_submit').click()
        time.sleep(10)
        
        
    def visit_ssl_manager(self):
        self.browser.find_element_by_id('item_ssl-manager').click()
        time.sleep(10)
        
        self.browser.find_element_by_css_selector('a[href="install.html"]').click()
        time.sleep(10)
        
        self.browser.find_element_by_css_selector('.update-link').click()
        time.sleep(10)
        
    def update_certificate(self):
        self.browser.find_element_by_id('sslcrt').click()
        self.browser.find_element_by_id('sslcrt').send_keys(open('./cert.pem', 'r').read())
        
        self.browser.find_element_by_id('sslkey').click()
        self.browser.find_element_by_id('sslkey').send_keys(open('./key.pem', 'r').read())
        
        time.sleep(5)
        self.browser.find_element_by_id('btnInstall').click()
        time.sleep(10)

    
CpanelImportCert().main()  
