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

results = []

soup = BeautifulSoup(browser.page_source, "html.parser")
# soup = BeautifulSoup(response.text, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")

jobs = job_list.find_all('li', recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        # it reflects the absent of something
        # h2 = job.find("h2", class_ = "jobTitle")
        # a = h2.find("a")
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            'link': f"https://kr.indeed.com{link}",
            'company': company.string,
            'location': location.string,
            'position': title,
        }
        results.append(job_data)
for result in results:
    print(result, "\n//////\n")
