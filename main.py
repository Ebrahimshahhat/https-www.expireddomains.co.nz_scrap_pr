#importing our used libraries
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import numpy as np
import requests
'''----------------------'''
def get_domain_per_page(i):
    new_url='https://www.expireddomains.co.nz/search.php?action=search&results_per_page=100&page='+str(i)
    r=requests.get(new_url)
    soup=BeautifulSoup(r.content,'html.parser')
    table = soup.find(id='result')
    rows=table.find_all('tr')
    domains=[]
    for i in range(1,len(rows)-1):
        cells=rows[i].findAll('td')
        domain=cells[1].get_text()
        domains.append(domain)
    return domains
if __name__=='__main__':
    pages=input("enter page numbers: ")
    all_domains=[]
    i=1
    while i<= int(pages):
        try:
            domains=get_domain_per_page(i)
            all_domains.extend(domains)
            print(f"page {i} scrapped successfully")
            i+=1
        except:
            print("error occured, clossing loop")
            break


    data = pd.DataFrame({'Country': all_domains})
    data.to_csv("data.csv",index=False)


