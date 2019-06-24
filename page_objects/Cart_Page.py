"""
This module models the cart page on weather shopper
URL: /cart
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators 

class Cart_Page(Base_Page):
    "This class models the cart page"

    CART_ROW = locators.CART_ROW
    CART_ROW_COLUMN = locators.CART_ROW_COLUMN
    COL_NAME = 0
    COL_PRICE = 1 

    def start(self):
        "Override the start method of base"
        url = "cart"
        self.open(url)

    def process_item(self,item):
        "Process the given item"
        #Convert the price to an int
        try:
            item[self.COL_PRICE] = int(item[self.COL_PRICE])
        except Exception as e:
            self.write("Unable to convert the string %s into a number"%item[self.COL_PRICE])

        return item 

    def get_cart_items(self):
        "Get all the cart items as a list of [name,price] lists"
        cart_items = []
        row_elements = self.get_elements(self.CART_ROW)
        for index,row in enumerate(row_elements):
            column_elements = self.get_elements(self.CART_ROW_COLUMN%(index+1))
            item = []
            for col in column_elements:
                text = self.get_dom_text(col)
                item.append(text.decode('ascii'))
            item = self.process_item(item)
            cart_items.append(item)

        return cart_items

    def verify_cart(self,product_list):
        "Verify the (name,price) of items in cart and the total"
        result_flag = False
        cart_items = self.get_cart_items()
        
        #Make sure expected and actual carts have the same number of items
        if len(cart_items) == len(product_list):
            result_flag = True
        
        self.conditional_write(result_flag,
        positive="The expected cart and actual cart have the same number of items: %d"%len(product_list),
        negative="The expected cart has %d items while the actual cart has %d items"%(len(product_list),len(cart_items)))

        #Is every item in the cart in our expected list?
        item_match_flag = True 
        for item in cart_items:
            #Does the item exist in the product list
            found_flag = False 
            price_match_flag = False 
            actual_price = 0
            for product in product_list:
                if product.name == item[self.COL_NAME]:
                    found_flag = True
                    if product.price == item[self.COL_PRICE]:
                        price_match_flag = True 
                    else:
                        actual_price = product.price
                    break
            self.conditional_write(found_flag,
            positive="Found the expected item %s in the cart"%item[self.COL_NAME],
            negative="Could not find the expected item %s in the cart"%item[self.COL_NAME])

            self.conditional_write(price_match_flag,
            positive="And the expected price matched to %d"%item[self.COL_PRICE],
            negative="BUT the expected price did not match. Expected: %d but Obtained: %d"%(actual_price,item[self.COL_PRICE]))

            item_match_flag &= found_flag and price_match_flag

        result_flag &= item_match_flag
        
        #Is every item on the expected list in the cart?
        if item_match_flag is False:
            pass
        """
        #Make sure expected and actual carts have the same number of items
        if len(cart_items) != len(product_list):
            for product in product_list:
                for item in cart_items:
                    if product.name
        """

        #result_flag = self.verify_name()
        #result_flag &= self.verify_price()
        return result_flag 