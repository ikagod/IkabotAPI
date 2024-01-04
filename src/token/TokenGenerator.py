import os
import random
from fake_useragent import UserAgent
from playwright.sync_api import sync_playwright


class TokenGenerator:
    """
    TokenGenerator class for generating tokens using Selenium.

    This class initializes a Selenium WebDriver with a headless Chrome browser and provides a method to retrieve tokens
    from game1.js.

    Usage:
    ```
    token_generator = TokenGenerator()
    token = token_generator.get_token()
    ```
    """

    def __init__(self):
        """
        Initialize TokenGenerator.

        - Initializes the Selenium WebDriver with a headless Chrome browser.
        - Sets the path to the HTML file used for token generation.
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.html_file_path = f"file:///{current_directory}/token.html"

    def get_token(self):
        """
        Get a token from the HTML file.

        Waits for the presence of a specific div element in the HTML file and returns its text content as the token.

        Returns:
        - str: The generated token.
        """
        with sync_playwright() as playwright:
            random_useragent = UserAgent().random
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context(user_agent=random_useragent)
            page = context.new_page()
            page.goto(self.html_file_path)
            token_element = page.wait_for_selector("body > div")
            token = token_element.inner_text()
            browser.close()
        return token

