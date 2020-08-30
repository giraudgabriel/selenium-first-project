import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)


def search(criteria):
    search_button = driver.find_element_by_class_name('search-expand')
    search_button.click()
    input_search = driver.find_element_by_name('q')
    input_search.send_keys(criteria)
    input_search.send_keys(Keys.ENTER)


def search_and_enter_page(criteria):
    search(criteria)
    time.sleep(2)
    try:
        div = driver.find_element_by_class_name('jump-link')
        print('Achei uma publicação que bate com o filtro')
        read_more = div.find_element_by_tag_name("a")
        time.sleep(1)
        read_more.click()
    except:
        print('Nenhum resultado encontrado!')


if __name__ == '__main__':
    filter = 'berinjela'
    path_website = 'http://gfgiraud.blogspot.com/'
    driver.get(path_website)
    search_and_enter_page(filter)
