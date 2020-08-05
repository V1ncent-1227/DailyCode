#!/usr/bin/env python3
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time

now = time.strftime('%Y-%m-%d', time.localtime())
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def webhook(result):
    webhookurl = "http://sc.ftqq.com/"
    sckey = "SCU107316Tdd0895f6697ccdad9e75ddc382cf35005f1e4ed7c5876" #替换成自己的sckey
    requests.get(url=webhookurl + sckey + ".send?text="+now+"&desp=" + result)

def logwrite(text):

    with open('../log.txt', 'a') as f:
        f.write(date + ' ' + text + '\n')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('window-size=1920x3000')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')

browser = webdriver.Chrome("./chromedriver", options=chrome_options)
browser.get('http://www.iwencai.com/stockpick/search?tid=stockpick&qs=box_main_ths&w=cci%E5%B0%8F%E4%BA%8E-100%E5%92%8Cj%E5%B0%8F%E4%BA%8E0%E5%92%8Ck%E5%B0%8F%E4%BA%8E30%E5%92%8Cd%E5%B0%8F%E4%BA%8E30%E5%92%8Cmacd%E5%B0%8F%E4%BA%8E0%E4%B8%8D%E5%8C%85%E5%90%ABst')
#print(browser.page_source)
trs = browser.find_elements_by_xpath('//*[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr')
result = ''
for tr in trs:
    code = tr.find_element_by_xpath('td[3]/div').text
    name = tr.find_element_by_xpath('td[4]/div/a').text
    #print(code, name)
    result += '* ' + code + ' ' + name + '\n'
    logwrite(code + ' ' + name)
#print(result)
webhook(result)
