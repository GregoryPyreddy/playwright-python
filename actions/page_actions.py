import asyncio

class PageActions:
    def check_clickable(self, page, selector):
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

    def enter_text(self, page, selector, text):
        try:
            element = page.query_selector(selector)
            if element:
                element.fill(text)
                print(f"Entered text '{text}' into element with selector '{selector}'.")
            else:
                print(f"No element found with selector '{selector}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def wait_for_element_to_be_clickable(self, page, selector):
        try:
            # Wait for the element to be visible and enabled
            page.wait_for_selector(selector, state='visible')
            page.wait_for_selector(selector, state='enabled')
            print(f"The element with selector '{selector}' is now clickable.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def enter_security_answer(self, page, locator, question):
        if question.lower().find('best friend') != -1:
            self.enter_text(page, locator, "Namrata")
        elif question.lower().find('color') != -1:
            self.enter_text(page, locator, "Red")
        elif question.lower().find('sports') != -1:
            self.enter_text(page, locator, "ManUtd")

    def get_text(self, page, selector):
        page.text_content(selector)

    def wait_for_element_to_be_present(self, page, selector, timeout=30000):
        try:
            # Wait for the element to be present in the DOM
            page.wait_for_selector(selector, timeout=timeout)
            print(f"The element with selector '{selector}' is now present in the DOM.")
        except Exception as e:
            print(f"An error occurred: {e}")