import requests
from bs4 import BeautifulSoup
import boto3
import pandas

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAYWRNZXYEZI4AYD5E',
    aws_secret_access_key = "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",
    region_name = 'us-west-2'
)

resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIAYWRNZXYEZI4AYD5E',
    aws_secret_access_key = "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",
    region_name = 'us-west-2'
)

clientResponse = client.list_buckets()
def upload_file(file_name, bucket, object_name=None):
    pass

URL = "https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=software%20developer%20intern&location=United%20States"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all("div", class_="base-search-card__info")

for list in jobs:
    title = list.find("h3", class_="base-search-card__title").text.strip()
    company = list.find("h4", class_="base-search-card__subtitle").text.strip()
    company_href = list.find_all(href=True)
    companyLink = []
    for el in company_href:
       companyLink.append(el['href'])
    location = list.find('div', class_="base-search-card__metadata").text
    shortLocation = " ".join(location.split())
    # print(title)
    # print(company)
    # print(companyLink)
    # print(shortLocation)

