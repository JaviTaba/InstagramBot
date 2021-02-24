from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


class InstagramBot:
    scrolls = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        user_name_acgt = driver.find_element_by_xpath("//input[@name='username']")
        user_name_acgt.clear()
        user_name_acgt.send_keys(self.username)
        password_acgt = driver.find_element_by_xpath("//input[@name='password']")
        password_acgt.clear()
        password_acgt.send_keys(self.password)
        password_acgt.send_keys(Keys.RETURN)
        time.sleep(10)
        # driver.find_element_by_partial_link_text('Ikke nå').click()
        # "//a[@href'/accounts/login']"
        # "//input[@name='username']"
        # "//input[@name='password']"

    def like_photo_from_hashtag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching for picrie link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for x in pic_hrefs:
            driver.get(x)
            botones = driver.find_elements_by_class_name('_8-yf5')
            for y in botones:
                if ((y.get_attribute('aria-label') == "Liker") and (y.get_attribute('height') == "24")):
                    y.click()

    # No esta terminado
    def like_photo_from_hashtag_with_comment(self, hashtag, comment):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching for picrie link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for x in pic_hrefs:
            driver.get(x)
            botones = driver.find_elements_by_class_name('_8-yf5')
            for y in botones:
                if ((y.get_attribute('aria-label') == "Liker") and (y.get_attribute('height') == "24")):
                    y.click()

    def follow_from_account(self, account, amount):
        if amount > 25:
            for i in range(1, int(amount / 25)):
                self.__follow_from_account(account, 25)

    def __follow_from_account(self, account, amount):
        self.amount = amount
        seguidos = 0
        driver = self.driver
        driver.get("https://www.instagram.com/" + account + "/")
        time.sleep(2)
        self.scrolls += int(amount / 7)

        botones = driver.find_elements_by_class_name('-nal3 ')
        for x in botones:
            if (x.get_attribute('href') == str("https://www.instagram.com/" + account + '/followers/')):
                x.click()
                fBody = driver.find_element_by_css_selector(".isgrP")
                for i in range(1, self.scrolls):
                    driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                    time.sleep(2)
                seguir = driver.find_elements_by_class_name("y3zKF")
                for x in seguir:
                    if seguidos < amount:
                        x.click()
                        time.sleep(3)
                        seguidos += 1
                    else:
                        break

    def unfollow_whitelisted(self, amount, *whitelist):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        unfollowed = 0

        botones = driver.find_elements_by_class_name('-nal3 ')
        for x in botones:
            if (x.get_attribute('href') == str("https://www.instagram.com/" + self.username + '/following/')):
                x.click()
                fBody = driver.find_element_by_css_selector('.isgrP')
                for i in range(0, int(amount / 7)):
                    driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                    time.sleep(2)

                usuario = driver.find_elements_by_css_selector('.HVWg4')
                for x in usuario:
                    username = usuario.find_element_by_css_selector('._0imsa')
                    print(username)
                    unfollow_button = usuario.find_element_by_css_selector('._8A5w5')
                    if not username in whitelist:
                        if unfollowed < amount:
                            unfollow_button.click()
                            unfollowed += 1
                        else:
                            break


