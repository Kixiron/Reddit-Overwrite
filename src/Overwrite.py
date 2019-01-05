import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = 'DangeFloof'
PASSWORD = '33031233'
MESSAGE = "This comment has been overwritten by an open source script to protect this user's privacy.  \nIf you would like to do the same, simply run [this python script]()"

driver = webdriver.Firefox()
driver.get('https://www.reddit.com/login')
driver.find_element_by_id('loginUsername').send_keys(USERNAME)
driver.find_element_by_id('loginPassword').send_keys(PASSWORD)
driver.find_element_by_class_name('AnimatedForm__submitButton').click()
current_url = driver.current_url
driver.get('https://old.reddit.com/user/{}/comments'.format(USERNAME))
comments = driver.find_elements_by_class_name('CommentListing__comment')
for comment in comments:
    buttons = comment.find_elements_by_class_name('CommentFlatList__item')
    edit_button = None
    delete_button = None
    for button in button:
        if button.get_attribute('innerHTML') == 'edit':
            edit_button = button
        elif button.get_attribute('innerHTML') == 'delete':
            delete_button = button
        if edit_button != None and delete_button != None:
            break
    edit_button.click()
    textarea = comment.find_element_by_class_name('MarkdownForm__text')
    textarea.clear()
    textarea.send_keys(MESSAGE)
    comment.find_element_by_class_name('MarkdownForm__submit').click()