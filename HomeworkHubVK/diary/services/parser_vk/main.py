from selenium import webdriver
from parse_functions import *


def main(names_discipline: list[str], mail_of_vk, password_of_vk):
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()

        authorization_on_vk(driver, mail_of_vk, password_of_vk)
        all_posts = parse_all_posts(driver, names_discipline)
        return all_posts

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
