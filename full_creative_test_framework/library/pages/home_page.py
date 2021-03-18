from time import sleep
from datetime import datetime
from library import AllLibraryMethods
from library.constants import JavaScriptConstants, HomePageConstants


class Homepage(AllLibraryMethods):
    def draw(self,type, co_ordinates, testcase=None):
        constant=''
        if type==HomePageConstants.line:
            constant=JavaScriptConstants.draw_line(co_ordinates)
        if type==HomePageConstants.rectangle:
            constant=JavaScriptConstants.draw_rectangle(co_ordinates)
        self.execute_js(constant)
        sleep(2)
        if testcase:
            self.log.info(str(testcase)+type+" is drawn")
            self.log.take_screenshot(ss_filename=str(testcase)+str(
                datetime.now().strftime("%m%d%Y_%H%M%S")) + '.jpg'.replace(" ", "_"))

    def erase(self, co_ordinates, testcase=None):
        self.execute_js(script=JavaScriptConstants.eraser(co_ordinates=co_ordinates))
        sleep(2)
        if testcase:
            self.log.info(str(testcase)+" Line is erased")
            self.log.take_screenshot(ss_filename=str(testcase) + str(
                datetime.now().strftime("%m%d%Y_%H%M%S")) + '.jpg'.replace(" ", "_"))


