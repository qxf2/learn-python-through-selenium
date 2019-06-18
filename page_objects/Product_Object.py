"""
This Object models the product page.
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Product_Object():
    "Page Object for the products object"
    PRODUCTS_LIST = locators.PRODUCTS_LIST

    def add_product(self,filter_condition):
        "Add the lowest priced product with the filter condition in name"
        pass