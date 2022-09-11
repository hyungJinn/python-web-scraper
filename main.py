from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# pls ignore above codes. Just it works Replit. It is not a big deal. 

# respose = get("https://www.indeed.com/jobs?q=python&limit=50")
# I'm never going to use above code. "Requset" is being blocked by indeed.com

browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
# soup = BeautifulSoup(response.text, "html.parser")

job_list = soup.find("ul", class_ = "jobsearch-ResultsList")

jobs = job_list.find_all('li', recursive=False)
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  if zone == None:
    # it reflects the absent of something
    
