import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

def export(results):
    df = pd.DataFrame(results)
    df.to_csv("indeed_job_results.csv", mode="a", index=False, header=True) 

def scrape_jobs():
    job_search = "Python+Developer"
    base_url = "https://in.indeed.com/"
    # https://in.indeed.com/jobs?q={job_search}&l=&from=searchOnHP
    url = base_url + f'jobs?q={job_search}&l=&from=searchOnHP'
    scraper = cloudscraper.create_scraper()
    # response = scraper.get(base_url)
    response = scraper.get(url)
    # print(response.status_code)
    bs = BeautifulSoup(response.text, "html.parser")
    # print(bs)
    #css-zu9cdh eu4oa1w0  ----container name-----
    job_list =  bs.find('ul', {'class':'css-zu9cdh'})
    # print(job_list)
    jobs = job_list.findAll('div',{'class':'job_seen_beacon'})
    # print(jobs)
    info = []
    o={}

    for job in jobs:
        Title = job.find('h2',{'class':'jobTitle'})
        title = Title.text
        link = Title.find('a').attrs['data-jk']
        # print(link,title)
        # https://in.indeed.com/viewjob?cmp=Maltech-Engineering-Services-Pvt-LTD&t=Python+Developer&jk=119e968f06a519e9&q=Python+Developer&xpse=SoCG67I3JVMFytwHBp0KbzkdCdPP&vjs=3
        url = f'https://in.indeed.com/viewjob?&t=Python+Developer&jk={link}&q=Python+Developer&xpse=SoCG67I3JVMFytwHBp0KbzkdCdPP&vjs=3'

        company_name = job.find('span', {"class":"companyName"}).text

        try:
              o["location"]=job.find('div',{"class":"companyLocation"}).text
        except:
              o["location"]=None
    
        try:
              o["salary"]=job.find('div',{"class":"css-1ihavw2"}).text
        except:
              o["salary"]=None

        data = {
            'title': title,
            'company_name':company_name,
            'company_location':o["location"],
            'url': url,
            'salary': o["salary"]
        }
        info.append(data)
    export(info)

if __name__ == "__main__":
    scrape_jobs()