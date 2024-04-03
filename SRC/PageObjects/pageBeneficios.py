import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException as ECIE, ElementNotInteractableException, \
    NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
from datetime import timedelta
import random


class PageBeneficios:

    def __init__(self, my_driver):
        self.driver = my_driver

