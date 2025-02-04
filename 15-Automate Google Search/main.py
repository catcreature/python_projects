from selenium import webdriver
from urllib.parse import quote_plus

search_string = input("Input the URL or string you want to search for: ")
search_string = quote_plus(search_string)
browser = webdriver.Edge('msedge.exe')
browser.get("https://www.google.com/search?q=" + search_string)