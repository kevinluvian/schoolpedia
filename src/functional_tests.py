from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_search_psle_score(self):
        # Kevin want to check the new website, schoolpedia to apply for secondary school

        self.browser.get('http://localhost:8000')
        # He notices the page title and header mention SchoolPedia
        self.assertIn('SchoolPedia', self.browser.title)
        # He is invited to enter his PSLE score right away
        inputbox = self.browser.find_element_by_id('pslescorehome')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter PSLE Score'
        )
        # He type his psle score 200
        inputbox.send_keys('200')

        # when he hit enter, the page updates and show the list of school
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the filter for psle score is 200
        inputbox = self.browser.find_element_by_id('scoreSchool')
        self.assertEqual(
            inputbox.get_attribute('value'),
            '200'
        )

        # there is "ADMIRALTY SECONDARY SCHOOL" in the school list
        table = self.browser.find_element_by_id('schoolListTable')
        rows = table.find_elements_by_class_name('header')
        self.assertTrue(
            any(row.text == 'ADMIRALTY SECONDARY SCHOOL' for row in rows)
        )

        # and then he quit
        print('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
