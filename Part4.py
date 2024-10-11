from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

service = Service(executable_path="D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

Name = []
Professor = []
Description = []
Session= []
Books= []
              
driver.get("http://eduko.spikotech.com/Course/Index")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll("div", attrs={"class": "sidebar-header hidden-sm-down"}):
    print(a)
    CourseName = a.find("h4",attrs = {"class":"card-title"})
    Teacher = a.find("h7")
    Desc = a.find("h7")
    session = a.find("p",attrs = {"class":"card-text"})
    href = a.find("a",attrs = {"class":"btn"})
    if CourseName != None and Teacher != None and Desc != None and session != None :
        Name.append(CourseName.text)
        Professor.append(Teacher.value) 
        Description.append(Desc.text)
        Session.append(session.Text) 
        Books.append(href.href)
    if len(Name) == 10:
        break

df = pd.DataFrame({"Name": Name, "Professor": Professor, "Description": Description, "Session":Session, "Books":Books })
df.to_csv("Part4Eduko.csv", encoding="utf-8")