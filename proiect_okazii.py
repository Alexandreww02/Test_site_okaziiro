##TEST CASE
## PLAN DE TESTARE


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests

#SETUP FOR BROWSER

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_homepage_status():
    url = "https://www.okazii.ro/"
    response = requests.get(url)

    # VERIFYING CODE OF STATUS HTTP

    assert response.status_code == 200, f"The status code is {response.status_code}, we are waiting 200"

    # VERIFYING LENGTH OF THE ANSWER

    assert len(response.text) > 0, "The response content is empty"


# TEST FOR SEARCH-BAR ON SITE

def test_shopping_cart(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:
        #CLOSE THE COOKIE TAB

        cookie_element = browser.find_element(By.ID,"cookiescript_accept")
        cookie_element.click()
        time.sleep(3)

        #SEARCH IN THE SEARCH-BAR

        search_bar = browser.find_element(By.NAME, "keyword")
        search_bar.send_keys("husa iphone 15 pro max")
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

        #ADD TO CART ONE PRODUCT

        add_to_cart = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[2]/figure/a/img")
        add_to_cart.click()
        time.sleep(2)

        #VIEW CART

        add_to_cart2 = browser.find_element(By.CSS_SELECTOR, "#btn_addProductToCart > span")
        add_to_cart2.click()
        time.sleep(2)

        #VIEW CART AND COMPLETE THE FIELDS

        view_cart = browser.find_element(By.XPATH, "/html/body/div[12]/div[1]/div/div/div[2]/div[1]/div[3]/a")
        view_cart.click()
        time.sleep(2)

        #COMPLETE THE FIELDS WITH DETAILS ABOUT COMMAND

        delivery_dates = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/button/span")
        delivery_dates.click()
        time.sleep(2)

        add_first_name = browser.find_element(By.ID, "u-address_firstname")
        add_first_name.send_keys("Marian")
        time.sleep(2)

        add_name = browser.find_element(By.ID,"u-address_lastname")
        add_name.send_keys("Popescu")
        time.sleep(2)

        phone_number = browser.find_element(By.ID, "u-address_mobile")
        phone_number.send_keys("0721015016")
        time.sleep(2)

        mail_adress = browser.find_element(By.ID, "u-address_email")
        mail_adress.send_keys("par@venitu.com")
        time.sleep(2)

        county = browser.find_element(By.ID, "u-address_county")
        county.send_keys("B" * 6)
        time.sleep(2)

        city = browser.find_element(By.ID, "u-address_city")
        city.send_keys("S" * 6)
        time.sleep(2)

        street = browser.find_element(By.ID, "u-address_street")
        street.send_keys("Maria margareta nistor")
        time.sleep(2)

        number_of_street = browser.find_element(By.ID, "u-address_number")
        number_of_street.send_keys("123")
        time.sleep(3)

        postal_code = browser.find_element(By.ID, "u-address_zipcode")
        postal_code.send_keys("915400")
        time.sleep(3)

        block_number = browser.find_element(By.ID, "u-address_building")
        block_number.send_keys("N32")
        time.sleep(3)

        floor = browser.find_element(By.ID, "u-address_floor")
        floor.send_keys("-")
        time.sleep(3)

        scale = browser.find_element(By.ID, "u-address_stair")
        scale.send_keys("A")
        time.sleep(3)

        apartment = browser.find_element(By.ID, "u-address_apartment")
        apartment.send_keys("77")
        time.sleep(3)

        
        delivery = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/button/span")
        delivery.click()
        time.sleep(3)



    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


#TEST FOR PART OF LOGIN

def test_login(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:


        cookie_element = browser.find_element(By.ID,"cookiescript_accept")
        cookie_element.click()
        time.sleep(3)

        login = browser.find_element(By.CSS_SELECTOR, "#login-trigger > span.orange.d-inline.b")
        login.click()
        time.sleep(2)

        email_login = browser.find_element(By.ID, "login_input")
        email_login.send_keys("florinaiulianardelean@gmail.com")
        time.sleep(2)

        password_login = browser.find_element(By.ID, "login_pass")
        password_login.send_keys("marianputernicul1")
        time.sleep(2)

        login = browser.find_element(By.NAME, "loginbtn")
        login.click()
        time.sleep(2)

        assert "Bine ai venit" in browser.page_source

    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")



#TEST FOR ADD AT FAVORITES

def test_favorites(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:

        cookie_element = browser.find_element(By.ID,"cookiescript_accept")
        cookie_element.click()
        time.sleep(3)

        search_bar = browser.find_element(By.NAME, "keyword")
        search_bar.send_keys("baterie externa")
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

        add_favorites = browser.find_element(By.CSS_SELECTOR, "#MostViewed-tracking-container > div > div > li.carousel-slide.slick-slide.slick-current.slick-active > div > a > div.item-detail > span")
        add_favorites.click()
        time.sleep(2)

        add_favorites_2 = browser.find_element(By.CSS_SELECTOR, "#btn_addToWatchList > span")
        add_favorites_2.click()
        time.sleep(2)

        email_login = browser.find_element(By.ID, "login_input")
        email_login.send_keys("florinaiulianardelean@gmail.com")
        time.sleep(2)

        password_login = browser.find_element(By.ID, "login_pass")
        password_login.send_keys("marianputernicul1")
        time.sleep(2)

        login = browser.find_element(By.NAME, "loginbtn")
        login.click()
        time.sleep(2)


    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


#TEST FOR FUNCTIONABILITY URL-s

def test_functionability_links(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:

        cookie_element = browser.find_element(By.ID,"cookiescript_accept")
        cookie_element.click()
        time.sleep(3)
        actions = ActionChains(browser)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        for _ in range(10):  
            actions.send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(3)

        redirect_link = browser.find_element(By.CSS_SELECTOR, "#Okazii-Footer > div.Footer-Container > div > div:nth-child(4) > ul > li > a")
        redirect_link.click()
        time.sleep(2)

        libra_pay = browser.find_element(By.CSS_SELECTOR, "#main > div.OKAZII-Blocks.clearfix > div > ul > li:nth-child(1) > h2 > a")
        libra_pay.click()
        time.sleep(2)

        accept_cookies_2 = browser.find_element(By.CSS_SELECTOR, "#cookieConsentStickyFooter > div > div > div.cookie-consent-col-md-4.cookie-consent-text-right > button")
        accept_cookies_2.click()
        time.sleep(2)


        assert "LibraPay" in browser.page_source
   
    
    
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")



#TEST SITE PROTOCOL

def test_protocol(browser):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:
   
        browser.get("https://www.okazii.ro/")
        
        browser.implicitly_wait(10)
        

    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")













        


