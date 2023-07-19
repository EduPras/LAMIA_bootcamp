from bs4 import BeautifulSoup
import requests
import time

print('Unfamiliar skill: ')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=programming&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in (enumerate(jobs)):
        publish_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name}')
                    f.write(f'Required skills: {skills}')
                    f.write(f'More info: {more_info}')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...\n')
        time.sleep(time_wait*60)
