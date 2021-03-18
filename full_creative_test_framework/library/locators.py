from selenium.webdriver.common.by import By


class HomepageLocators:
    draw_line_icon= By.XPATH ,'//*[@id="editor"]//input[contains(@title,"line")]'
    canvas_board= By.XPATH, '//*[@id="imageTemp"]'