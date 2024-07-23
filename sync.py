from playwright.sync_api import sync_playwright

def check_clickable(page, selector):
    try:
        element = page.query_selector(selector)
        if element:
            # Check if the element is visible
            visible = element.is_visible()
            # Check if the element is enabled
            enabled = element.is_enabled()
            if visible and enabled:
                print(f"The element with selector '{selector}' is clickable.")
            else:
                print(f"The element with selector '{selector}' is not clickable.")
        else:
            print(f"No element found with selector '{selector}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_text(page, selector, text):
    try:
        element = page.query_selector(selector)
        if element:
            element.fill(text)
            print(f"Entered text '{text}' into element with selector '{selector}'.")
        else:
            print(f"No element found with selector '{selector}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def wait_for_element_to_be_clickable(page, selector):
    try:
        # Wait for the element to be visible and enabled
        page.wait_for_selector(selector, state='visible')
        page.wait_for_selector(selector, state='enabled')
        print(f"The element with selector '{selector}' is now clickable.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_security_answer(page, locator, question):
    if question.lower().find('best friend') != -1:
        enter_text(page, locator, "Namrata")
    elif question.lower().find('color') != -1:
        enter_text(page, locator, "Red")
    elif question.lower().find('sports') != -1:
        enter_text(page, locator, "ManUtd")

def get_text(page, selector):
    try:
        element = page.query_selector(selector)
        if element:
            text = element.inner_text()
            print(f"The text content of the element with selector '{selector}' is: {text}")
            return text
        else:
            print(f"No element found with selector '{selector}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def wait_for_element_to_be_present(page, selector, timeout=30000):
    try:
        # Wait for the element to be present in the DOM
        page.wait_for_selector(selector, timeout=timeout)
        print(f"The element with selector '{selector}' is now present in the DOM.")
    except Exception as e:
        print(f"An error occurred: {e}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://odxui.dev02.odx-nonprod.o360.cloud/ncc")
    wait_for_element_to_be_clickable(page, '#username')
    page.click('#username')
    enter_text(page, '#username', 'gpyreddy')
    enter_text(page, '#login-pwd', 'Sid@1806')
    wait_for_element_to_be_clickable(page, '#btnLogin')
    page.click('#btnLogin')
    wait_for_element_to_be_present(page, '#lbl_secAnswer')
    enter_security_answer(page, '#secAnswer', get_text(page, '#lbl_secAnswer'))
    page.click('#continuebtn')
    wait_for_element_to_be_present(page, "h1#table-caption")
    print("in security page")