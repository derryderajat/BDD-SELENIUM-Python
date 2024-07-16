# from selenium import webdriver
from selenium import webdriver


def before_scenario(context, step):
    context.driver = webdriver.Chrome()
    context.driver.get("https://thetestingworld.com/testings/")

def after_scenario(context,step):
    context.driver.close()