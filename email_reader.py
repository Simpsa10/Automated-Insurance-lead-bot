from flask import Flask, request
from selenium import webdriver
import time
import pyautogui

app = Flask(__name__)

@app.route('/sms', methods = ['POST'])

def sms():
    string = "Please"
    message_body = request.form['Body']
    newstr = message_body.split(string, 1)[0]

    exePay(newstr)

    print('Link: ',newstr)

    return str(newstr)

def exePay(newstr):
    web = webdriver.Chrome()
    web.get(str(newstr))

    time.sleep(2)

    CSV = "###" # Enter user's credit card CSV
    CSVText = web.find_element_by_xpath('//*[@id="TxtCardCSV"]')
    check = web.find_element_by_xpath('//*[@id="LblTC"]')
    secondCheck = web.find_element_by_xpath('//*[@id="btnAcceptTC"]')
    payNow = web.find_element_by_xpath('//*[@id="btnPayNow"]')

    CSVText.send_keys(CSV)
    check.click()
    secondCheck.click()
    payNow.click()

    # Get around googles bot protection use manual click
    pyautogui.click(740, 223)

if __name__ == '__main__':
    app.run()



