import requests
from bs4 import BeautifulSoup
searchstring=input("Enter phone name")
url="https://www.flipkart.com/search?q="+searchstring
#set HTML
raw=requests.get(url)
htmlContent=raw.content
#Parsing the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
#html tree traversal
container = soup.findAll("a", {"class": "s1Q9rs"})
container2=soup.find_all("div",{"class":"_4rR01T"})
phone_list=[]
if len(container) != 0:
    for phone in container:
        phone_list.append(phone["title"])
else:

    for phone in container2:
        phone_list.append(phone.text)
container2_product_link=container2=soup.find_all("a", {"class": "_1fQZEK"})
container_product_link=container2=soup.find_all("a", {"class": "s1Q9rs"})
product_link=[]
if len(container)!=0:
    for link in container_product_link:
        product_link.append("https://www.flipkart.com"+link["href"])
else:
    for link in container2_product_link:
        product_link.append("https://www.flipkart.com"+link["href"])
#getting price
product_detail = {}
i=0
for phone_name, link in zip(phone_list, product_link):
    if(i<10):
        product_raw = requests.get(link)
        product_html = product_raw.content
        product_soup = BeautifulSoup(product_html, 'html.parser')
        price = product_soup.find_all("div", {"class": "_30jeq3 _16Jk6d"})[0].text
        product_detail[phone_name] = [{"price": price}]
        i+=1
    else:
        break
print(product_detail)
