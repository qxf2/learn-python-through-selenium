"""
This class models the landing page of Weather Shopper.
URL: /
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

class Main_Page(Base_Page):
    "Page Object for the main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
