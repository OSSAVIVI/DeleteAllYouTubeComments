import time

class KillComments:
    def __init__(self, driver):
        for i in range(0, 100000):  # 100,000 is the default number of comments to delete (change as needed)
            click_3_dots(driver)
            click_trash_can(driver)
            kill_final_alert(driver)
            time.sleep(2)
            driver.refresh()
            time.sleep(2.2)
        print("Shutting down in 5 seconds :)")
        time.sleep(5)
        driver.close()


def kill_final_alert(driver):
    body = driver.find_element_by_xpath('/html/body')
    yt_app = body.find_element_by_xpath('ytd-app')
    pop_up = yt_app.find_element_by_xpath('ytd-popup-container')
    time.sleep(.05)
    dialog = pop_up.find_element_by_xpath('paper-dialog')
    confirm = dialog.find_element_by_xpath('yt-confirm-dialog-renderer')
    div = confirm.find_element_by_id('main')
    buttons = div.find_element_by_xpath('div')
    conf_btns = buttons.find_element_by_id('confirm-button')
    link = conf_btns.find_element_by_xpath('a')
    link.click()


def click_trash_can(driver):
    time.sleep(2)
    body = driver.find_element_by_xpath('/html/body')
    yt_app = body.find_element_by_xpath('ytd-app')
    pop_up = yt_app.find_element_by_xpath('ytd-popup-container')
    drop_down = pop_up.find_element_by_xpath('iron-dropdown')
    div0 = drop_down.find_element_by_id('contentWrapper')
    time.sleep(.1)
    menu_rend = div0.find_element_by_xpath('ytd-menu-popup-renderer')
    list_box = menu_rend.find_element_by_xpath('paper-listbox')
    time.sleep(.1)
    menu_navs = list_box.find_elements_by_xpath('ytd-menu-navigation-item-renderer')
    # access SECOND element in menu_navs for trash can...
    if menu_navs.__len__() == 2:
        link = menu_navs[1].find_element_by_xpath('a')
        link.click()
    else:
        link = menu_navs[0].find_element_by_xpath('a')
        link.click()
    time.sleep(1)


def click_3_dots(driver):
    time.sleep(2)
    body = driver.find_element_by_xpath('/html/body')
    yt_app = body.find_element_by_xpath('ytd-app')
    time.sleep(.1)
    div0 = yt_app.find_element_by_id("content")
    page_mgr = div0.find_element_by_xpath('ytd-page-manager')
    time.sleep(.1)
    browse = page_mgr.find_element_by_xpath('ytd-browse')
    two_col_browse = browse.find_element_by_xpath('ytd-two-column-browse-results-renderer')
    div1 = two_col_browse.find_element_by_id("primary")
    list_rend = div1.find_element_by_xpath('ytd-section-list-renderer')
    time.sleep(1)
    div2 = list_rend.find_element_by_id("contents")
    section_rend = div2.find_element_by_xpath('ytd-item-section-renderer')
    time.sleep(1)
    div3 = section_rend.find_element_by_id("contents")
    comment_entry = div3.find_element_by_xpath('ytd-comment-history-entry-renderer')
    time.sleep(.1)
    div4 = comment_entry.find_element_by_id("menu")
    menu_rend = div4.find_element_by_xpath('ytd-menu-renderer')
    time.sleep(.1)
    yt_button = menu_rend.find_element_by_xpath('yt-icon-button')
    button = yt_button.find_element_by_xpath('button')
    time.sleep(.1)
    button.click()
