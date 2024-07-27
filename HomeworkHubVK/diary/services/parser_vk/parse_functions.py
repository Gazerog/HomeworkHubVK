from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import pickle
import re


def authorization_on_vk(driver, mail, password_of_vk):
    driver.get('https://vk.com')
    time.sleep(5)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(mail)
    email_input.send_keys(Keys.ENTER)
    time.sleep(25)

    try:
        password_input = driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password_of_vk)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
    except NoSuchElementException:
        pass

    pickle.dump(driver.get_cookies(), open('cookies', 'wb'))
    time.sleep(2)
    return driver


def get_date_posts_on_page(driver):
    posts_content = []
    page_wall_posts = driver.find_element(By.ID, 'page_wall_posts')
    for wall_text in page_wall_posts.find_elements(By.CLASS_NAME, 'wall_text'):
        try:
            text = wall_text.find_element(By.CLASS_NAME, 'wall_post_text').text
            wall_hrefs = wall_text.find_element(By.CLASS_NAME, 'SecondaryAttachmentGroup')
            wall_hrefs.find_elements(By.CLASS_NAME, 'SecondaryAttachment')
        except NoSuchElementException:
            continue
        date_string = text.split('/n')[0]
        posts_content.append(re.findall(r'\b\d{2}\.\d{2}\.\d{2}(?:\d{2})?\b',
                                        date_string))
    return posts_content


def parse_all_posts(driver, disciplines) -> list:
    all_vk_posts = []
    for i in disciplines:
        driver.get(f'https://vk.com/wall-222259259?q={i.replace(" ", "%20")}')
        time.sleep(3)

        for cookie in pickle.load(open('cookies', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(5)

        quantity_posts = int(driver.find_element(By.ID, 'fw_summary').text)
        redundant_posts = quantity_posts % 20
        quantity_pages = (quantity_posts - redundant_posts) // 20

        for number_page in range(quantity_pages + 1):
            driver.get(f'https://vk.com/wall-222259259?q={i.replace(" ", "%20")}&offset={number_page * 20}')
            time.sleep(5)
            all_vk_posts = all_vk_posts + [{'discipline': disciplines[i],
                                           'date': get_date_posts_on_page(driver)}]
    return all_vk_posts
