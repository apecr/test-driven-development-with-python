import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")

    yield browser

    browser.quit()


# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep


def test_title_is_ok(browser):
    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title


def test_assert_h1_correct_value(browser):
    # She notices the page title and header mention to-do lists
    header_text = browser.find_element_by_tag_name('h1').text

    assert 'To-Do' in header_text


def test_enter_a_to_do_list_straight_away(browser):
    # She is invited to enter a to-do item straight away
    input_box = browser.find_element_by_id('id_new_item')

    assert input_box.get_attribute('placeholder') == 'Enter a to-do item'


def test_create_first_to_do_list_element(browser):
    input_box = browser.find_element_by_id('id_new_item')
    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)
    input_box.send_keys('Buy peacock feathers')
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)

    table = browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    assert '1: Buy peacock feathers' in rows[0].text


def test_create_two_to_do_list_elements(browser):
    input_box = browser.find_element_by_id('id_new_item')
    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)
    input_box.send_keys('Buy peacock feathers')
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)
    input_box = browser.find_element_by_id('id_new_item')
    input_box.send_keys('Use peacock feathers to make a fly')
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)

    table = browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    assert '1: Buy peacock feathers' in rows[0].text
    assert '2: Use peacock feathers to make a fly' in rows[0].text
