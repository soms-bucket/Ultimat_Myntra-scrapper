import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import sqlite3

def process():


       page_request = requests.get(url, headers=headers)


       soup = bs(page_request.text,"html.parser")
              ##print(soup)

       web_page=soup.find_all('script')[11]
       web_page=str(web_page)[22:-9].strip()
        ##print(web_page)

       data=json.loads(web_page)
       data_ln=len(data["searchData"]["results"]["products"])
              ##print(data_ln)
       for d_ln in range(50):
 

              #website
              website_nm="https://www.myntra.com"
              Website_.append(website_nm)
              #print(website_nm)

              #product link
              prdct_link=website_nm+"/"+data["searchData"]["results"]["products"][d_ln]["landingPageUrl"]
              Product_Link.append(prdct_link)
              #print(prdct_link)

              #product name
              prdtc_name=data["searchData"]["results"]["products"][d_ln]["productName"]
              Product_Name.append(prdtc_name)##################
              #print(prdtc_name)

              #product brand
              prdtc_brand=data["searchData"]["results"]["products"][d_ln]["brand"]
              Product_Brand.append(prdtc_brand)
              #print(prdtc_brand)

              #product category
              prdtc_cate=data["searchData"]["results"]["products"][d_ln]["category"]
              Product_Category.append(prdtc_cate)
              #print(prdtc_cate)

              #product size
              prdtc_size=data["searchData"]["results"]["products"][d_ln]["sizes"]
              #prdtc_size=prdtc_size.split(",")
              #prdtc_size_lst=[prdtc_size[i] for i in range(len(prdtc_size))]

              Sizes_Available.append(prdtc_size)
              #print(prdtc_size)

              #product price
              prdtc_price=data["searchData"]["results"]["products"][d_ln]["price"]
              Price_.append(prdtc_price)
              #print(prdtc_price)

              #product mrp
              prdtc_mrp=data["searchData"]["results"]["products"][d_ln]["mrp"]
              MRP_.append(prdtc_mrp)
              #print(prdtc_mrp)

              #product gender
              prdtc_gndr=data["searchData"]["results"]["products"][d_ln]["gender"]
              Gender_.append(prdtc_gndr)
              #print(prdtc_gndr)

              #product description
              prdtc_dscpt=prdtc_brand+" "+prdtc_gndr+" "+prdtc_cate+" , Current Price: "+str(prdtc_price)
              Description_.append(prdtc_dscpt)
              #print(prdtc_dscpt)

              #primary image
              prdtc_pimg=data["searchData"]["results"]["products"][d_ln]["searchImage"]
              Primary_Image_Link.append(prdtc_pimg)
              #print(prdtc_pimg)

              #secondary images
              Secondary_Image_lll=[]
              prdtc_simg=data["searchData"]["results"]["products"][d_ln]["images"]
              prdtc_simg_lst=[]
              ###########
              for simg in range(len(prdtc_simg)):

                     if prdtc_simg[simg]["src"] == "" or prdtc_simg[simg]["src"] == prdtc_pimg :
                            continue
                     else:
                            ##print(type(prdtc_simg[simg]["src"]))
                            prdtc_simg_lst.append(prdtc_simg[simg]["src"])

              prdtc_simg_lst=list(set(prdtc_simg_lst))

              for ppp in range(len(prdtc_simg_lst)):

                     Secondary_Image_lll.append(prdtc_simg_lst[ppp])

              b=Secondary_Image_lll
              ##print(b)
              ##print("\n\n\n")
              Secondary_Image_lll=[]

              f=""
              for i in range(len(b)):
                     f= f+"   "+b[i]
              f=f.strip()    
              #Secondary_Image_lll.append(c)
              Secondary_Image_Links.append(f)


              ##print(simg) 16 min
              #print("\n")
              #print(len(prdtc_simg))             
              ##print(prdtc_simg_lst)
              #print("\n\n\n\n")
              ##print("\n\n\n\n\n\n\n\n\n\n")#############################################
              ##print(Secondary_Image_Links)
              #print("\n\n\n\n")


              #Secondary_Image_Links=[]


       """
       #Database #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#

       conn = sqlite3.connect('myntra_data.db')
       c = conn.cursor()

       #delete table
       #c.execute('''DROP TABLE ultimate''')

       #create a table
       c.execute('''CREATE TABLE ultimate(Website_ text,Product_Link text,Product_Name text,Product_Brand text,Product_Category text,Sizes_Available text,Price_ int,MRP_ int,Gender_ text,Description_ text,Primary_Image_Link text,Secondary_Image_Links text)''')

       #data to insert

       """
       for ddd in range(len(Website_)):

              c.execute('''INSERT INTO ultimate VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (Website_[ddd],Product_Link[ddd],Product_Name[ddd],Product_Brand[ddd],Product_Category[ddd],Sizes_Available[ddd],Price_[ddd],MRP_[ddd],Gender_[ddd],Description_[ddd],Primary_Image_Link[ddd],Secondary_Image_Links[ddd]))
              conn.commit()

       #select all data from table and #print
       c.execute('''SELECT * FROM ultimate''')
       results = c.fetchall()
       ##print(results)








###############################################################


def process1():


       page_request = requests.get(url, headers=headers)


       soup = bs(page_request.text,"html.parser")
              ##print(soup)

       web_page=soup.find_all('script')[11]
       web_page=str(web_page)[22:-9].strip()
        ##print(web_page)

       data=json.loads(web_page)
       data_ln=len(data["searchData"]["results"]["products"])
              ##print(data_ln)
       for d_ln in range(1):
 

              #website
              website_nm="https://www.myntra.com"
              Website_.append(website_nm)
              #print(website_nm)

              #product link
              prdct_link=website_nm+"/"+data["searchData"]["results"]["products"][d_ln]["landingPageUrl"]
              Product_Link.append(prdct_link)
              #print(prdct_link)

              #product name
              prdtc_name=data["searchData"]["results"]["products"][d_ln]["productName"]
              Product_Name.append(prdtc_name)##################
              #print(prdtc_name)

              #product brand
              prdtc_brand=data["searchData"]["results"]["products"][d_ln]["brand"]
              Product_Brand.append(prdtc_brand)
              #print(prdtc_brand)

              #product category
              prdtc_cate=data["searchData"]["results"]["products"][d_ln]["category"]
              Product_Category.append(prdtc_cate)
              #print(prdtc_cate)

              #product size
              prdtc_size=data["searchData"]["results"]["products"][d_ln]["sizes"]
              #prdtc_size=prdtc_size.split(",")
              #prdtc_size_lst=[prdtc_size[i] for i in range(len(prdtc_size))]

              Sizes_Available.append(prdtc_size)
              #print(prdtc_size)

              #product price
              prdtc_price=data["searchData"]["results"]["products"][d_ln]["price"]
              Price_.append(prdtc_price)
              #print(prdtc_price)

              #product mrp
              prdtc_mrp=data["searchData"]["results"]["products"][d_ln]["mrp"]
              MRP_.append(prdtc_mrp)
              #print(prdtc_mrp)

              #product gender
              prdtc_gndr=data["searchData"]["results"]["products"][d_ln]["gender"]
              Gender_.append(prdtc_gndr)
              #print(prdtc_gndr)

              #product description
              prdtc_dscpt=prdtc_brand+" "+prdtc_gndr+" "+prdtc_cate+" , Current Price: "+str(prdtc_price)
              Description_.append(prdtc_dscpt)
              #print(prdtc_dscpt)

              #primary image
              prdtc_pimg=data["searchData"]["results"]["products"][d_ln]["searchImage"]
              Primary_Image_Link.append(prdtc_pimg)
              #print(prdtc_pimg)

              #secondary images
              Secondary_Image_lll=[]
              prdtc_simg=data["searchData"]["results"]["products"][d_ln]["images"]
              prdtc_simg_lst=[]
              ###########
              for simg in range(len(prdtc_simg)):

                     if prdtc_simg[simg]["src"] == "" or prdtc_simg[simg]["src"] == prdtc_pimg :
                            continue
                     else:
                            ##print(type(prdtc_simg[simg]["src"]))
                            prdtc_simg_lst.append(prdtc_simg[simg]["src"])

              prdtc_simg_lst=list(set(prdtc_simg_lst))

              for ppp in range(len(prdtc_simg_lst)):

                     Secondary_Image_lll.append(prdtc_simg_lst[ppp])

              b=Secondary_Image_lll
              ##print(b)
              ##print("\n\n\n")
              Secondary_Image_lll=[]

              f=""
              for i in range(len(b)):
                     f= f+"   "+b[i]
              f=f.strip()    
              #Secondary_Image_lll.append(c)
              Secondary_Image_Links.append(f)


              ##print(simg) 16 min
              #print("\n")
              #print(len(prdtc_simg))             
              ##print(prdtc_simg_lst)
              #print("\n\n\n\n")
              ##print("\n\n\n\n\n\n\n\n\n\n")#############################################
              ##print(Secondary_Image_Links)
              #print("\n\n\n\n")


              #Secondary_Image_Links=[]


       """
       #Database #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#

       conn = sqlite3.connect('myntra_data.db')
       c = conn.cursor()

       #delete table
       #c.execute('''DROP TABLE ultimate''')

       #create a table
       c.execute('''CREATE TABLE ultimate(Website_ text,Product_Link text,Product_Name text,Product_Brand text,Product_Category text,Sizes_Available text,Price_ int,MRP_ int,Gender_ text,Description_ text,Primary_Image_Link text,Secondary_Image_Links text)''')

       #data to insert

       """
       for ddd in range(len(Website_)):

              c.execute('''INSERT INTO ultimate VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (Website_[ddd],Product_Link[ddd],Product_Name[ddd],Product_Brand[ddd],Product_Category[ddd],Sizes_Available[ddd],Price_[ddd],MRP_[ddd],Gender_[ddd],Description_[ddd],Primary_Image_Link[ddd],Secondary_Image_Links[ddd]))
              conn.commit()

       #select all data from table and #print
       c.execute('''SELECT * FROM ultimate''')
       results = c.fetchall()
       ##print(results)




Website_=[]
Product_Link=[]
Product_Name=[]
Product_Brand=[]
Product_Category=[]
Sizes_Available=[]
Price_=[]
MRP_=[]
Gender_=[]
Description_=[]
Primary_Image_Link=[]
Secondary_Image_Links=[]



#Database [header:] #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#


conn = sqlite3.connect('myntra_data.db')
c = conn.cursor()
#delete table
#c.execute('''DROP TABLE ultimate''')

#create a table
c.execute('''CREATE TABLE ultimate(Website_ text,Product_Link text,Product_Name text,Product_Brand text,Product_Category text,Sizes_Available text,Price_ int,MRP_ int,Gender_ text,Description_ text,Primary_Image_Link text,Secondary_Image_Links text)''')

############################

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
# the page about to scrape

#Clothing********************************************
print("Starting Ultimate:\n\n")
print("Collecting Clothings....")
gen="men"
for i in range(2):

       for page in range(2300):
              url="https://www.myntra.com/"+gen+"-clothings?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"



#Footwear********************************************

gen="men"
for i in range(2):

       for page in range(600):
              url="https://www.myntra.com/"+gen+"-footwear?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"

print("Collecting Footwear....")

#watches********************************************

gen="men"
for i in range(2):

       for page in range(100):
              url="https://www.myntra.com/"+gen+"-watches?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"

print("Collecting watches....")

# Wallets*************************************************

gen="men"
for i in range(2):

       for page in range(60):
              url="https://www.myntra.com/"+gen+"-wallets?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"

print("Collecting Wallets....")

#bags***************************************************

for page in range(120):
       url="https://www.myntra.com/men-bags?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(362):
       url="https://www.myntra.com/women-bags?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting bags/backpacks....")

#Jewellery***********************************************

for page in range(40):
       url="https://www.myntra.com/men-jewellery?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(500):
       url="https://www.myntra.com/women-jewellery?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Jewellery....")

#Belts***************************************************

for page in range(100):
       url="https://www.myntra.com/men-belts?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(20):
       url="https://www.myntra.com/women-belts?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Jewellery....")

#Ties**************************************************

for page in range(40):
       url="https://www.myntra.com/men-ties?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1):
       url="https://www.myntra.com/ties-girls"

       #print(page+1)
              
       process1()

print("Collecting Ties....")

# Cufflinks*******************************************

for page in range(20):
       url="https://www.myntra.com/men-cufflinks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1):
       url="https://www.myntra.com/cufflinks-women?p=1&plaEnabled=false"

       #print(page+1)
              
       process1()

print("Collecting Cufflinks....")

#Pocket Squares****************************************

for page in range(20):
       url="https://www.myntra.com/pocket-squares-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Pocket-Squares....")

#Caps and Hats********************************************

for page in range(20):
       url="https://www.myntra.com/caps-for-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1):
       url="https://www.myntra.com/hats-for-men?p=1&plaEnabled=false"

       #print(page+1)
              
       process1()

for page in range(2):
       url="https://www.myntra.com/hats-for-women?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Caps-and-Hats....")

#Mufflers, Scarves and Gloves*******************************

for page in range(30):
       url="https://www.myntra.com/mufflers,-scarves-and-gloves?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Mufflers, Scarves and Gloves....")

# Phones Cases***********************************************

for page in range(14):
       url="https://www.myntra.com/phones-cases?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Phones Cases....")

#Rings and Wristwear*****************************************

for page in range(3):
       url="https://www.myntra.com/rings-and-wristwear-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(40):
       url="https://www.myntra.com/rings-and-wristwear-women?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Rings and Wristwear....")

# Socks***********************************************************  

for page in range(50):
       url="https://www.myntra.com/men-socks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(20):
       url="https://www.myntra.com/women-socks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Socks....")

# Bracelets**********************************************************

for page in range(10):
       url="https://www.myntra.com/men-bracelets?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(50):
       url="https://www.myntra.com/women-bracelets?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Bracelets....")

# Chains**********************************************************

for page in range(3):
       url="https://www.myntra.com/men-chains?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()


for page in range(6):
       url="https://www.myntra.com/women-chains?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

print("Collecting Chains....")




#Database[ending] #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#

#close database connection
conn.close()












