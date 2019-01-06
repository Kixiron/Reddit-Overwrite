import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MESSAGE = "This comment was deleted to protect the original poster's privacy and security.  \nIf you also value your privacy, you can do the same by simply running [this python script](https://github.com/Kixiron/Reddit-Overwrite)"

def login():
    print('Please input login info for Reddit (This is not stored or transmitted)')
    USERNAME = input('Username: ')
    PASSWORD = input('Password: ')
    print('Logging in...')
    driver.get('https://www.reddit.com/login')
    driver.find_element_by_id('loginUsername').send_keys(USERNAME)
    driver.find_element_by_id('loginPassword').send_keys(PASSWORD)
    driver.find_element_by_class_name('AnimatedForm__submitButton').click()
    driver.get('https://old.reddit.com/user/{}/comments'.format(USERNAME))
    input('Make sure you\'re logged in to the proper reddit account and then press Enter to continue')
    return USERNAME

def delete_page_comments():
    comment_num = 0
    for comment in comments:
        comment_num += 1
        buttons = comment.find_elements_by_class_name('CommentFlatList__item')
        edit_button = None
        delete_button = None
        for button in buttons:
            if button.get_attribute('innerHTML') == 'edit':
                edit_button = button
            elif button.get_attribute('innerHTML') == 'delete':
               delete_button = button
            if edit_button != None and delete_button != None:
                break
        edit_button.click()
        try:
            textarea = comment.find_element_by_class_name('MarkdownForm__text')
            textarea.clear()
            textarea.send_keys(MESSAGE)
            comment.find_element_by_class_name('MarkdownForm__submit').click()
            delete_button.click()
            comment.find_element_by_class_name('RestrictedFlatlistButton__toggleOption').click()
            print('Deleted comment')
        except:
            print('Failed to delete comment')
            pass
    return comment_num

driver = webdriver.Firefox()
USERNAME = login()
print('Are you sure you want to delete all comments from your profile?')
confirmation = input('This is irrevocable and the script writer withdraws all responsibility for anything that happens\n')
if confirmation.lower() != 'yes' or confirmation.lower() != 'y':
    print('Deleting all comments will commence!')
    print('Note that this may take a while and might sometimes require you to re-run the script because of Reddit ratelimiting')
    print('While the script is running, try not to mess with the window opened by it')
    comment_num = 0
    while 1:
        driver.get('https://old.reddit.com/user/{}/comments'.format(USERNAME))
        print('Loaded new page of comments, deleting...')
        comments = driver.find_elements_by_class_name('CommentListing__comment')
        if len(comments) < 1:
            print('All comments have been deleted from your profile!')
            print('I deleted {} total comments'.format(comment_num))
            print('It is recommended that you go through what remains of your comment history to check if all comments were deleted properly')
            print('If something went wrong, please open an issue here: https://github.com/Kixiron/Reddit-Overwrite/issues/new')
            input('Press Enter to Exit')
            exit()
        else:
            comment_num += delete_page_comments()
else:
    print('Aborting...')
    exit()

