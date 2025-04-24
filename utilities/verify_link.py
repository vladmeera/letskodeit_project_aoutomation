from socks import HTTPError
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

class LinkVerification:

    PROTOCOLS = {"HTTPProtocol": "http://", "HTTPSProtocol": "https://"}
    TLD = {"com": ".com", "ru": ".ru", "org": ".org", "net": ".net"}
    ENDINGS = ("/", "//", "?", "!", "@")

    def verify_link (self, link):

        driver = webdriver.Chrome()

        test = "login-password"
        path = os.path.dirname(__file__)
        print(f"path is {path}")

        full_path = os.path.join(path, "..", "tests")
        print(full_path)

        _locators = {"login_link": "//a[text()='Sign In']", "email_field": "email",
                      "password_field": "login-password", "login_btn": "login"}
        for _locator in _locators:
            if test in _locators.get(_locator):
                print("Yes")
                break

        functions = {"run": "available", "swim": "not available", "jump": "available", }
        for i in functions:
            print(functions[i])

        link = link.strip()

        last_in_link = link[-1:]
        if last_in_link in self.ENDINGS:
            link = link.strip(last_in_link)

        domain_name = link[-3:]

        website_no_protocol = link.strip("https://")
        print(website_no_protocol)


        if not self.PROTOCOLS["HTTPSProtocol"] in link:
            return False
        else:

            print("https was used")
            link = link.strip("https://")


        if domain_name in self.TLD:
            print(f"Domain name: {domain_name}")
        elif self.TLD["ru"] in domain_name:
            return False
        else:
            raise UserWarning(f"Wierd domain name!!! - {domain_name}")









def main():
    verification = LinkVerification()
    verification.verify_link("https://www.letskodeit.com")

if __name__ == '__main__':
    main()