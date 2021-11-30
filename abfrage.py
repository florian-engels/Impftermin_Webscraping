from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import winsound
import beepy
import time

if __name__ == '__main__':
    weiter = True
    count = 0
    wartezeit = True

    driver = webdriver.Firefox()
    driver.get("https://001-iz.impfterminservice.de/impftermine/service?plz=68163")
    text = "Virtueller"
    while wartezeit:
        time.sleep(5)
        if (text in driver.page_source):
            wartezeit = True
        else:
            wartezeit = False

    time.sleep(2)
    try:
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Auswahl')]")
        for btn in buttons:
            btn.click()
    except:
        print()

    text2 = "Es wurden keine freien Termine"
    text3 = "Bitte warten, wir suchen"
    while weiter:
        if (text3 not in driver.page_source):
            if (text2 in driver.page_source):
                weiter = True
                buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Nein')]")
                for btn in buttons:
                    btn.click()
            else:
                for i in range(2):
                    beepy.beep(sound='success')
                weiter = False
        else:
            time.sleep(0.1)
            weiter = True




    #
    #     if (text in driver.page_source):
    #         print("Anzahl Aufrufe: %d" % count)
    #         weiter = True
    #         driver.close()
    #     else:
    #         weiter = False
    #
    # for i in range(1):
    #     beepy.beep(sound='success')
    #     #beepy.beep(sound='ready')
    #     #beepy.beep(sound='wilhelm')
