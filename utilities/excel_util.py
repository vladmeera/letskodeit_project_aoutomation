import openpyxl, os
import pandas as pd
import utilities.custom_logger as cl


class ExcelLocators:
    log = cl.custom_logger()

    def __init__(self, file):
        self.file = file

    def get_locator(self, page_name="login", locator_name="email field", locator_type="xpath"):

        try:
            df = pd.read_excel(self.file)
            row = df.index[(df['page name'] == page_name)
                                       & (df['locator name'] == locator_name)
                                       & (df['locator type'] == locator_type)].tolist()
            if df.iloc[row[0]]["locator"] is not None:
                self.log.info(f"Locator was found using |> {locator_name} | name |> on --> ***{page_name}*** page")
                return df.iloc[row[0]]["locator"]
        except Exception as e:
            self.log.error(f"| {locator_name} |> locator on -> {page_name} page was not found in '{self.file}' --> {e}")



class ExcelAccounts:
    log = cl.custom_logger()

    def __init__(self, file):
        self.file = file


    def get_login(self, account_id=1, valid_invalid="valid"):

        try:
            df = pd.read_excel(self.file)
            row = df.index[(df['account id'] == account_id) & (df['valid/invalid'] == valid_invalid)].tolist()
            if df.iloc[row[0]]["login"] is None:
                self.log.error(f"Account was not found using {account_id} id with ***{valid_invalid}***")
                return None
            else:
                self.log.info(f"Was found 1 account with login - {df.iloc[row[0]]["login"]} | ***{valid_invalid}***")
                return df.iloc[row[0]]["login"]
        except Exception as e:
            self.log.error(f"Something went wrong - {e}")

    def get_password(self, account_id=1, valid_invalid="valid"):

        try:
            df = pd.read_excel(self.file)
            row = df.index[(df['account id'] == account_id) & (df['valid/invalid'] == valid_invalid)].tolist()
            if df.iloc[row[0]]["password"] is None:
                self.log.error(f"Account was not found using {account_id} id and ***{valid_invalid}***")
                return None
            else:
                self.log.info(f"Was found 1 account with password - {df.iloc[row[0]]["password"]} | ***{valid_invalid}***")
                return df.iloc[row[0]]["password"]
        except Exception as e:
            self.log.error(f"Something went wrong - {e}")


# current_dir = os.path.dirname(__file__)
# excel_files_path = os.path.join(current_dir, "..")
# excel_locators_file = os.path.join(excel_files_path, "accounts.xlsx")
#
# locators = ExcelAccounts(excel_locators_file)
#
# print(locators.get_login())
# print(locators.get_password())