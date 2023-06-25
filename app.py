import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
 
# "RowContent.CompUnitStatsContainer.CompUnitTraitsContainer.UnitContainer.Unit_Wrapper.UnitNames"

# Launch Chrome browser in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
 
# Load web page
browser.get("https://www.metatft.com/comps")
# Network transport takes time. Wait until the page is fully loaded
def is_ready(browser):
    return browser.execute_script(r"""
        return document.readyState === 'complete'
    """)
WebDriverWait(browser, 30).until(is_ready)
 
# Scroll to bottom of the page to trigger JavaScript action
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(browser, 30).until(is_ready)
 
# Search for news CompRow and print
CompRows= browser.find_elements(By.CSS_SELECTOR, "div.CompRow")

f=open("data.txt", "a")

for elem in CompRows:
    unit_names=elem.find_elements(By.CSS_SELECTOR, 'div.UnitNames')
    comp_title=elem.find_element(By.CSS_SELECTOR, 'div.Comp_Title')
    f.write("SET: " + comp_title.text + "\nInclude: ")
    for unit in unit_names:
        print(unit.text, end=" ")
        f.write(unit.text + " ")
    f.write("\n")
f.close()

# Close the browser once finish
browser.close()