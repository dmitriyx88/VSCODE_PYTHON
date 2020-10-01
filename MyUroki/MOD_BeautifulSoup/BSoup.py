import bs4 
import requests
file= open(r"c:\\olx_ua.txt", "a")
glubina=4
url1= "https://www.olx.ua/"
domain = "www.olx.ua"
links_list=[]
links_ok=[]

def bs_funk(urls):
    page= requests.get(urls)
    ss= bs4.BeautifulSoup(page.text, features="lxml")
    
    
    for links in bs4.BeautifulSoup.find_all(ss, "a"):
        if links.get("href"):
            if domain in links["href"] and links["href"] not in links_list:
                links_list.append(links["href"])
    ph= bs4.BeautifulSoup.find(ss, "xx-large")
    print(ph)
        
def writefile(stringa):
    file= open(r"c:\\olx_ua.txt", "a")
    file.write(stringa+"\n")
    file.close()

bs_funk(url1)

for i in range(glubina):
    for y in range(len(links_list)):
        if links_list[y] not in links_ok:        
            writefile(str(links_list[y]))
            bs_funk(links_list[y])
            links_ok.append(links_list[y])
        

