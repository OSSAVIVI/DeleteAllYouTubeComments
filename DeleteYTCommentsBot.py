import time


class DeleteYTCommentsBot:
    def __init__(self, driver):
        time.sleep(4)
        find_sign_in_button(driver)


def find_sign_in_button(driver):
    button_number = 0
    all_buttons = driver.find_elements_by_id('button')
    for button in all_buttons:
        button_number += 1
        button_name = button.get_attribute('aria-label').__str__()
        if button_name == "Sign in":
            button.click()
            time.sleep(3)
            break

    body = driver.find_element_by_xpath("/html/body")
    all_divs = body.find_elements_by_xpath("div")
    rec_view_cont_search(all_divs)
    rec_view_cont_search.looking_for_next = True
    rec_view_cont_search(all_divs)

    time.sleep(5)


def rec_view_cont_search(divs):
    # create static variable to handle break statements in recursion to prevent multiple entries of username
    rec_view_cont_search.entered_username = getattr(rec_view_cont_search, 'entered_username', False)
    rec_view_cont_search.looking_for_next = getattr(rec_view_cont_search, 'looking_for_next', False)
    div_number = 0
    for div in divs:  # parse parent divs
        if rec_view_cont_search.entered_username and not rec_view_cont_search.looking_for_next:  # already found username, so break recursion
            break
        div_number += 1
        view_conts = div.find_elements_by_id("view_container")
        view_conts_length = view_conts.__len__()
        if view_conts_length > 0:  # Detect input boxes
            view_cont_number = 0
            for view_cont in view_conts:  # Search through div_containers (if any)
                view_cont_number += 1
                more_divs = view_cont.find_elements_by_xpath("div")
                more_divs_length = more_divs.__len__()
                if more_divs_length > 0:
                    if not rec_view_cont_search.looking_for_next:
                        rec_form_search(more_divs)
                    else:
                        rec_next_search(more_divs)
        more_divs = div.find_elements_by_xpath("div")
        more_divs_length = more_divs.__len__()
        if more_divs_length > 0:
            rec_view_cont_search(more_divs)


def rec_form_search(divs):
    div_number = 0
    for div in divs:  # parse parent divs
        if rec_view_cont_search.entered_username and not rec_view_cont_search.looking_for_next:  # already found username, so break recursion
            break
        div_number += 1
        forms = div.find_elements_by_xpath("form")
        forms_length = forms.__len__()
        if forms_length > 0:  # Detect input boxes
            form_number = 0
            for form in forms:  # Search through forms (if any)
                form_number += 1
                method_type = form.get_attribute('method').__str__()
                if method_type == "post":  # determine if input is for email
                    span = form.find_element_by_xpath("span")
                    if span is not None:
                        section = span.find_element_by_xpath("section")
                        if section is not None:
                            form_span_section_divs = section.find_elements_by_xpath("div")
                            rec_input_search(form_span_section_divs)
        more_divs = div.find_elements_by_xpath("div")
        more_divs_length = more_divs.__len__()
        if more_divs_length > 0:
            rec_form_search(more_divs)


def rec_input_search(divs):
    div_number = 0
    for div in divs:  # parse parent divs
        if rec_view_cont_search.entered_username and not rec_view_cont_search.looking_for_next:  # already found username, so break recursion
            break
        div_number += 1
        input_boxes = div.find_elements_by_xpath("input")
        input_boxes_length = input_boxes.__len__()
        if input_boxes_length > 0:  # Detect input boxes
            for input_box in input_boxes:  # Search through input boxes (if any)
                type_name = input_box.get_attribute('type').__str__()
                if type_name == "email":  # determine if input is for email
                    input_box.send_keys("U")  # enter credentials
                    time.sleep(.5) # sleep tags are to mimic human input, but are actually no longer necessary, but keeping it in for now in case this changes again
                    input_box.send_keys("S")  # enter credentials
                    time.sleep(.2)
                    input_box.send_keys("E")  # enter credentials
                    time.sleep(.1)
                    input_box.send_keys("R")  # enter credentials
                    time.sleep(.5)
                    input_box.send_keys("N")  # enter credentials
                    time.sleep(.2)
                    input_box.send_keys("A")  # enter credentials
                    time.sleep(.1)
                    input_box.send_keys("M")  # enter credentials
                    time.sleep(.6)
                    input_box.send_keys("E")  # enter credentials
                    time.sleep(.2)
                    rec_view_cont_search.entered_username = True
                    break
        more_divs = div.find_elements_by_xpath("div")
        more_divs_length = more_divs.__len__()
        if more_divs_length > 0:
            rec_input_search(more_divs)


def rec_next_search(divs):
    div_number = 0
    for div in divs:  # parse parent divs
        if rec_view_cont_search.entered_username and not rec_view_cont_search.looking_for_next:
            break
        div_number += 1
        next_buttons = div.find_elements_by_id("identifierNext")
        next_buttons_length = next_buttons.__len__()
        if next_buttons_length > 0:  # Detect input boxes
            for next_button in next_buttons:  # Search through input boxes (if any)
                next_button.click()
                rec_view_cont_search.looking_for_next = False
                break
        more_divs = div.find_elements_by_xpath("div")
        more_divs_length = more_divs.__len__()
        if more_divs_length > 0:
            rec_next_search(more_divs)
