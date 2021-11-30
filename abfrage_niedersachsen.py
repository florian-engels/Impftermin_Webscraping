from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import winsound
import beepy
import time

if __name__ == '__main__':
    weiter = True
    count = 0
    wartezeit = True

    driver = webdriver.Firefox()
    driver.get("https://www.impfportal-niedersachsen.de/portal/#/appointment/public")

    driver.find_element_by_name("datenschutz").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    driver.find_element_by_name("bi").send_keys("02.10.1959")
    driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    # driver.find_element_by_id("mat-radio-9").click()
    # driver.find_element_by_xpath("//*[contains(text(), 'Verstanden')]").click()
    # driver.find_element_by_id("mat-radio-12").click()
    # driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    # driver.find_element_by_xpath("//*[contains(text(), 'Weiter')]").click()
    driver.find_element_by_name("zipCode").send_keys("49074")

    text = "Keine Termine"
    weiter = True
    while weiter:
        driver.find_element_by_xpath("//*[contains(text(), 'Suchen')]").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if (text in driver.page_source):
            weiter = True
        else:
            weiter = False
            for i in range(2):
                beepy.beep(sound='success')

    print("Termin auswählen")
