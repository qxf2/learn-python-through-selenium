from .Base_Page import Base_Page
from .product_object import Product_Object
import conf.locators_conf as locators

class Payment_Object(Product_Object):
    "Class for all the Payment objects"

    #locators   
    page_title = locators.page_title    
    pay_with_card = locators.pay_with_card  
    iframe_name = locators.iframe_name    
    email_field = locators.email 
    card_number_field = locators.card_number
    card_expiry_date_field = locators.card_expiry
    cvc_field = locators.cvc
    zip_code_field = locators.zip_code
    pay_button = locators.pay_button        

        
    def make_payment_with_card(self):
        "Make the payment for the items"
        result_flag = self.click_pay_with_card()
        result_flag &= self.switch_to_stripe_payment_gateway(self.iframe_name)

        return result_flag        

    def switch_to_stripe_payment_gateway(self,iframe_name):
        "Switch to payment gateway"        
        result_flag = self.switch_frame(self.iframe_name)
        self.conditional_write(result_flag,
            positive='Switched the frame: %s'%iframe_name,
            negative='Failed to switch the frame',
            level='debug')
       
        return result_flag

    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_field,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag    

    def set_card_number(self,card_number):
        "Set the card number on the form"
        result_flag = self.set_text(self.card_number_field,card_number)
        self.conditional_write(result_flag,
            positive='Set the card number to: %s'%card_number,
            negative='Failed to set the card number in the form',
            level='debug')

        return result_flag  

    def set_card_expiry_date(self,card_expiry):
        "Set the card expiry date(mm/yy) on the form"
        result_flag = self.set_text(self.card_expiry_date_field,card_expiry)
        self.conditional_write(result_flag,
            positive='Set the card expiry date to: %s'%card_expiry,
            negative='Failed to set the expiry date in the form',
            level='debug')

        return result_flag

    def set_cvc(self,cvc):
        "Set the cvc on the form"
        result_flag = self.set_text(self.cvc_field,cvc)
        self.conditional_write(result_flag,
            positive='Set the cvc to: %s'%cvc,
            negative='Failed to set the cvc in the form',
            level='debug')

        return result_flag 

    def set_zip_code(self,zip_code):
        "Set the zip code on the form"
        result_flag = self.set_text(self.zip_code_field,zip_code)
        self.conditional_write(result_flag,
            positive='Set the zip code to: %s'%zip_code,
            negative='Failed to set the zip_code in the form',
            level='debug')

        return result_flag

    def click_pay_with_card(self):  
        "Click on the pay with card button"      
        result_flag = self.click_element(self.pay_with_card)        
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay with card" button',
            negative='Failed to click on "Pay with card" button',
            level='debug')

        return result_flag

    def click_pay_button(self):      
        "Click on the pay(payment gateway) button"  
        result_flag = self.click_element(self.pay_button)        
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay" button',
            negative='Failed to click on "Pay" button',
            level='debug')

        return result_flag     

    def submit_payment_details(self,email,card_number,card_expiry,cvv,zip_code):
        "Submit the payment details"       
        result_flag = self.click_pay_button()        

        return result_flag 

    def get_title(self):
        "get title"
        title = self.get_text(self.page_title)

        return title 

        
