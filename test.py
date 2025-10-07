import csv
import pandas as pd
from utilities import data_util
from utilities import util

random_string = util.Util()
string_ = random_string.get_alpha_numeric(length=8, char_type='mix')
print(string_)


data = data_util.TestData('utilities/locators.csv')

# data.add_new_locator('login_button', 'xpath', 'sdffdsfdf123')
reader = pd.read_csv('utilities/locators.csv')
print(reader)

try:
    locator = reader[reader['element_name'] == 'login_button']
    locator_ = locator.values[-1]
    print(str(locator_[2]))
except KeyError:
    print(f'')

# data.add_new_locator("profile_icon", 'css', 'dsfdh2u22hj')

locator = data.get_locator('profile_icon')
print(f"Locator is - {locator}")