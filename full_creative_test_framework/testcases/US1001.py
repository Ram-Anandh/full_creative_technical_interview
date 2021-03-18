__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

from time import sleep
from selenium.webdriver.common.keys import Keys
from library import AllLibraryMethods
from library.locators import HomepageLocators
from library.constants import HomePageConstants


class US1001(AllLibraryMethods):

    def tc_first_case(self):
        """
            Dummy testcase to check the logo of the website
            Author           : Ram Anandh
            Testcase number  : 1000
        """

        # Step-1: Launch html_canvas website
        self.launch_website(title=HomePageConstants.page_title,testcase=1)

        # Step-2: Click on the draw line icon
        self.click_element(locator=HomepageLocators.draw_line_icon, testcase=2)

        # Step-3: Draw one vertical line
        self.draw(type=HomePageConstants.line,co_ordinates=(264, 55, 266, 221), testcase=3)

        # Step-4: Draw one horizontal line 160, 123);
        # context.lineTo(380, 122
        self.draw(type=HomePageConstants.line,co_ordinates=(160, 123, 380, 122), testcase=4)

        # Step-5: Draw a rectangle
        self.draw(type=HomePageConstants.rectangle,co_ordinates=(157, 289, 199, 97),
                       testcase=5)
        # Step-6: Erase Horizontal line
        self.erase(co_ordinates=(160, 123, 380, 122), testcase=6)
