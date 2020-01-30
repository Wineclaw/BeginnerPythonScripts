# A script that pulls the date and calculates net calories from MyFitnessPal
# for d number of days in the past and outputs the information in a text file

# Version: 0.1.1 — February 12, 2019
# By:   Jonathan Ace Wienclaw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def get_date(html):
    """ Scrapes 'html' and retuns an "unformatted" date"""
    dateline = html
    dateline_scrape = dateline.find('time')
    dateline_text = dateline_scrape.text
    dateline_text = dateline_text.strip()
    date = dateline_text
    return date


def format_month(month):
    """ Formats month in variable month_to_format """
    months = [("January", 1), ("February", 2), ("March", 3),
              ("April", 4), ("May", 5), ("June", 6),
              ("July", 7), ("August", 8), ("September", 9),
              ("October", 10), ("November", 11),
              ("December", 12)]
    for (name, num) in months:
        if name == month:
            return num


def get_total_cals(html):
    """ Scrapes 'html' and returns the total calories for the day """
    totals = html
    total_scrape = totals.find('tr', class_='total')
    total_line = total_scrape.text
    total_cals = total_line.split('\n')[2]
    total_cals = total_cals.replace(',', '')
    total_cals = int(total_cals)
    return total_cals


def get_ex_cals(html):
    """ Scrapes 'html' and returns the total calories for the day """
    exline = html
    try:
        exline_scrape = exline.find('td', class_='extra')
        exline_line = exline_scrape.text
        ex_cals = int(exline_line.split(' ')[12])
        return ex_cals
    except AttributeError:
        ex_cals = 0
        return ex_cals


def exportable_info():
    print(formatted_month, date_of_month,  year, sep='/', end="")
    print(",", net_cals)


def get_days():
    d = int(input("Please the number the number of days, starting from yesterday, you'd \
             like to pull data for?"))
    print("Thanks. Beginning data pull...")
    return d


# Login information
user = "fakeemail@gmail.com"
passw = "fakepassword"

# Sets number of days to pull from AFTER MOST RECENT DAY
# Ex: 90 days of data, d = 89
d = 0
d = get_days()


# Sets up browser and goes to MFP login page
browser = webdriver.Chrome(
    executable_path=r"C:/Coding/Project PastFood/chromedriver.exe")
wait = WebDriverWait(browser, 10)
browser.get('https://www.myfitnesspal.com/food/diary')


# Logs into MFP
userElem = browser.find_element_by_id('username')
userElem.send_keys(user)
passwElem = browser.find_element_by_id('password')
passwElem.send_keys(passw)
passwElem.submit()

# Brings us to a "data pull" page
prevdaybutton = wait.until(EC.presence_of_element_located
                           ((By.CLASS_NAME, "icon-caret-left")))
prevdaybutton.click()

# Sets var that passes off selenium to BS in scraping functions
html = BeautifulSoup(browser.page_source, 'lxml')

# This splits date scraped into just name of the month, "unformatted" month
dateline = get_date(html)
year = dateline.split(', ')[2]
dateline = dateline.split(',')[1]
unfor_month = dateline.split(' ')[1]
date_of_month = dateline.split(' ')[2]  # Splits out date to var

# Changes unformatted dateline to excel exportable date and assigns it to var
formatted_month = str(format_month(unfor_month))

# Assigns result of subtracting total calories from exercise calories to var
net_cals = get_total_cals(html) - get_ex_cals(html)

# Prints exportable information; date, net calories
with open('MFP_data.txt', 'w') as f:
    print(formatted_month, date_of_month,  year, sep='/', end="", file=f)
    print(",", net_cals, file=f)

# Loads next page
# And enters for loop pulling data and amending txt file for d days
for i in range(d):
    prevdaybutton = wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "icon-caret-left")))
    prevdaybutton.click()
    html = BeautifulSoup(browser.page_source, 'lxml')  # This line is required
    time.sleep(1)
    dateline = get_date(html)
    year = dateline.split(', ')[2]
    dateline = dateline.split(',')[1]
    unfor_month = dateline.split(' ')[1]
    date_of_month = dateline.split(' ')[2]
    formatted_month = str(format_month(unfor_month))
    net_cals = get_total_cals(html) - get_ex_cals(html)
    with open('MFP_data.txt', 'a') as f:
        print(formatted_month, date_of_month,
              year, sep='/', end="", file=f)
        print(",", net_cals, file=f)

# exits out of selenium, let's user know script is complete
browser.close()
browser.quit()
print("Output created in directory. Browser closed.")
