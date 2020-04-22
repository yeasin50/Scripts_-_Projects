import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import time

import csv

class NewEggGPU():
    def __init__(self, myurl,save=0):
        self.myurl = myurl
        uClient = uReq(myurl)
        page_html = uClient.read()
        uClient.close()
        page_soup =soup(page_html, "html.parser")
        containers = page_soup.findAll('div',{"class":"item-container"})
        
        self.containers = containers
        self.save= save
        

    def FirstPage(self):
        containers = self.containers
        save = self.save

        if save>0:
            filename = "GPUproduct.csv"
            f = open(filename, 'w+')
            headers ="brand, product_title, Item Price, Shipping\n"
            f.write(headers)

        for container in containers:
            info = container.find('div',{'class':'item-info'})

            titleSpan=container.findAll('a',{"class":"item-brand"})
            brand =''
            if len(titleSpan)>0 :
                brand = titleSpan[0].img['title'].title()
            else :
                brand ="cann't get"
            priceC = container.find('li',{"class":"price-current"}).text
            title = info.find('a',{'class':'item-title'}).text
            shipping = info.find('li',{"class":"price-ship"}).text.strip()
            
            # lining Error in price
            p =priceC.replace("\n","").replace(",",'')
            sS =''
            
            for i in p:
                if i == '(':
                    break
                else: sS+=i
            
            s =sS.replace(" ",'')
            print(s)
            if s == '-':
                continue
            else:
                if save==0:
                    print( 'brand '+brand ,'title '+title ,'shipping '+ shipping)
                    # print(s)
                

                elif save>0:
                    f.write(brand+ "," + title.replace(',', '|')+ "," +"," + shipping+ "\n")

        if save>0:
            f.close()

    def dataCollection(self, page_url):
        time.sleep(3)
        pageU = None

        pageU = page_url
        uClient = uReq(pageU)
        time.sleep(2)
        page_html = uClient.read()
        uClient.close()
        page_soup =soup(page_html, "html.parser")
        containers = page_soup.findAll('div',{"class":"item-container"})
        
        save = self.save

        if save>0:
            filename = "productSs.csv"
            f = open(filename, 'a+')
            # headers ="brand, product_Name, Shipping\n"
            # f.write(headers)

        for container in containers:
            info = container.find('div',{'class':'item-info'})

            titleSpan=container.findAll('a',{"class":"item-brand"})
            brand =''
            if len(titleSpan)>0 :
                brand = titleSpan[0].img['title'].title()
            else :
                brand ="cann't get"
            
            title = info.find('a',{'class':'item-title'}).text
            shipping = info.find('li',{"class":"price-ship"}).text.strip()
            priceC = container.find('li',{"class":"price-current"}).text
            
            price = priceC.replace("\n",'').replace(",",'').replace("\xa0",'').replace('-','')

             # lining Error in price
            p =priceC.replace("\n","").replace(",",'')
            sS =''
            
            for i in p:
                if i == '(':
                    break
                else: sS+=i
            
            s =sS.replace(" ",'')
            print(s)
            if s == '-':
                print("-_-")
                continue

            else:
                if save==0:
                    print( 'brand '+brand ,'title '+title,"pricing "+ price +' shipping '+ shipping)
                
                elif save>0:
                    f.write(brand+ "," + title.replace(',', '|')+"," + shipping+ "\n")

        if save>0:
            f.close()


    def nexPagesGenarate(self,  n=2):
        nextpagePageUrl = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-'
        print("fetching "+ str(n))

        for i in range(2,n):
            pageUrl = nextpagePageUrl+str(i)

            print('Loading >> '+ str(i)+"\n"+ pageUrl)

            self.dataCollection(pageUrl)
    
    



gpuurl ='https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

# secondPageUrl = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-2'

egg = NewEggGPU(gpuurl,3)
print('Graphics Card info')
egg.FirstPage()
egg.nexPagesGenarate(3)