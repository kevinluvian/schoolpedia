from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import os

env = os.getenv('PROD', False)
if env == 'True':
    DEBUG = False
else:
    DEBUG = True


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_search_psle_score(self):
        print('Kevin want to check the new website, schoolpedia to apply for secondary school')
        self.browser.get('http://localhost:8000')
        if DEBUG:
            inp = input()
        time.sleep(1)

        print('He notices the page title and header mention SchoolPedia')
        self.assertIn('SchoolPedia', self.browser.title)
        if DEBUG:
            inp = input()

        print('He is invited to enter his PSLE score right away')
        inputbox = self.browser.find_element_by_id('pslescorehome')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter PSLE Score'
        )
        if DEBUG:
            inp = input()

        print('He type his psle score 200')
        inputbox.send_keys('200')
        if DEBUG:
            inp = input()

        print('When he hit enter, the page updates and show the list of school')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        if DEBUG:
            inp = input()

        print('The filter for psle score is 200')
        inputbox = self.browser.find_element_by_id('scoreSchool')
        self.assertEqual(
            inputbox.get_attribute('value'),
            '200'
        )
        if DEBUG:
            inp = input()

        print('There is "ADMIRALTY SECONDARY SCHOOL" in the school list')
        table = self.browser.find_element_by_id('schoolListTable')
        rows = table.find_elements_by_class_name('header')
        self.assertTrue(
            any(row.text == 'ADMIRALTY SECONDARY SCHOOL' for row in rows)
        )
        if DEBUG:
            inp = input()

        print('Then, he open the admirality secondary school, to know its detail address')
        link = self.browser.find_element_by_link_text('ADMIRALTY SECONDARY SCHOOL')
        link.click()
        if DEBUG:
            inp = input()
        time.sleep(1)

        print('Kevin wants to leave a comment here, but it turns out he need to log in')
        link = self.browser.find_element_by_id('loginToReview')
        link.click()
        time.sleep(1)
        if DEBUG:
            inp = input()

        print('Kevin put the login account there')
        usernamebox = self.browser.find_element_by_id('id_username')
        usernamebox.send_keys('kevin@kevin.com')
        passwordbox = self.browser.find_element_by_id('id_password')
        passwordbox.send_keys('kevinkeren')
        if DEBUG:
            inp = input()
        passwordbox.send_keys(Keys.ENTER)
        time.sleep(1)

        print('It brings kevin to the previous page')
        school_name = self.browser.find_element_by_id('schoolName')
        self.assertTrue(school_name.text == 'ADMIRALTY SECONDARY SCHOOL')
        if DEBUG:
            inp = input()

        print('He left a comment there')
        write_review_button = self.browser.find_element_by_id('reviewBtn')
        write_review_button.click()
        commentbox = self.browser.find_element_by_id('id_message')
        commentbox.send_keys('This is the best school!')
        commentbox.send_keys(Keys.ENTER)
        if DEBUG:
            inp = input()
        time.sleep(1)

        # and then he quit
        print('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
