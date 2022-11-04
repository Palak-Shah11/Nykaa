from selenium.webdriver.common.by import By

search_bar = (By.XPATH, '//div[@id="app"]//input[@placeholder="Search for products, styles, brands"]')

product_name = (By.XPATH, '//div[@id="app"]//span[text()="Anarkali Sets for Women"]')

product_img = (By.XPATH, '//div[@id="app"]//img[@src="https://adn-static1.nykaa.com/nykdesignstudio-images/pub/media/catalog/product/7/9/tr:w-275,/798fabdBBCASS109_1.jpg?rnd=20200526195200"]')

size_s = (By.XPATH, '//div[@id="app"]//button[text()="S"]')

add_to_bag = (By.XPATH, '//div[@id="pdp-bottom-cta-container"]/button[text()="Add to Bag"]')

view_bag = (By.XPATH, '//div[@id="pdp-bottom-cta-container"]/button[text()="View bag"]')

proceed_to_buy = (By.XPATH, '//div[@id="app"]//button[text()="Proceed to Buy"]')

iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Nykaa Fashion Cart"]')

got_it_button_iframe = (By.XPATH, '//div[@id="portal-root"]//button[contains(text(), "Got it")]')

proceed_to_pay = (By.XPATH, '//div[@id="app"]//button[@data-at="continue-to-checkout"]')

move_to_wishlist =(By.XPATH, '//div[@id="app"]//button[contains(text(),"Move to Wishlist")]')

back_to_shopping = (By.XPATH, '//div[@id="app"]//button[contains(text(),"Back to shopping")]')

wishlist = (By.XPATH, '//div[@id="app"]//div[text()="Wishlist"]')
 # hjosihjp
