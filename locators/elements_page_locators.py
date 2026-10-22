

class TextBoxPageLocators:

    """form fields"""
    FULL_NAME = "css selector", "#userName"
    EMAIL = "css selector", "#userEmail"
    CURRENT_ADDRESS = "css selector", "#currentAddress"
    PERMANENT_ADDRESS = "css selector", "#permanentAddress"
    SUBMIT = "css selector", "#submit"


    """created form"""
    CREATED_FULL_NAME  =  "css selector", "#output #name"
    CREATED_EMAIL  =  "css selector", "#output #email"
    CREATED_CURRENT_ADDRESS  =  "css selector", "#output #currentAddress"
    CREATED_PERMANENT_ADDRESS  =  "css selector", "#output #permanentAddress"


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = "css selector", ".rc-tree-switcher"
    ITEM_LIST = "css selector", "span[class='rc-tree-checkbox']"
    CHECKED_ITEMS = "css selector", ".rc-tree-checkbox-checked"
    TITLE_ITEM = "css selector", "rc-tree-title"
    OUTPUT_RESULT = "css selector", "span[class='text-success']"
    # ['desktop', 'notes', 'commands', 'downloads', 'wordFile', 'excelFile']