# A script that pulls the date and total calories from MyFitnessPal
# for X number of days in the past and outputs the information in a text file.
# Uses mechanicalsoup for hopefully faster results.

# Version: 0.1 — January 29, 2020
# By:   Jonathan Ace Wienclaw

import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
test = browser.open("https://www.myfitnesspal.com/food/diary")

# fills out form with login details and submits
browser.select_form('form[action="https://www.myfitnesspal.com/account/login"]'
                    )
browser["username"] = "fakeemail@gmail.com"
browser["password"] = "fakepassword"
browser.submit_selected()


def get_days():
    """Prompts user for number of days to pull data for"""
    d = int(input("How many days would you like to pull data for?"))
    print("Thanks. Beginning data pull...")
    return d


# starts the entire script!
d = 0
d = get_days()

# After submitting the login information, we should be at the first page for
# data extraction. Then we run our first page pull.
# Pulls page data
page = browser.get_current_page()

# We then list out items near the total calories number, and isolate the total
# calorie number; total calories is the 3rd item, hence the [3]
total = list(page.find('tr', class_="total"))[3].text
print(total)
with open('testdata.txt', 'a') as f:
    print(total, file=f)

# For loop for pulling data for every page after the initial day
for i in range(d):
    # Possible definition for any data pulls past the first day
    # moves on to next page
    p = browser.find_link(class_='prev')
    browser.follow_link(p)
    print(browser.get_url())
    # Both page and total need to be zeroed out for some reason before
    # pulling the next day
    page = 0
    page = browser.get_current_page()
    total = 0
    total = list(page.find('tr', class_="total"))[3].text
    # print checks that we got the total
    print(total)
    with open('testdata.txt', 'a') as f:
        print(total, file=f)

# Final printed message
print('Output created in directory. Data pull complete. Thank you!')
