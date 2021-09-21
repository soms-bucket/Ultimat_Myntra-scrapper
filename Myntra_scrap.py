import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import sqlite3
from random import randint as rn

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
       for d_ln in range(data_ln):
 

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

################################## Product Category Page Number ########################################
#max 2300 page
Clothing=1

#max 600 page
Footwear=1

#max 100 page
watches=1

#max 60 page
Wallets=1

#max 120 page
bags_1 =1

#max 362 page
bags_2 =1

#max 40 page
Jewellery_1 =1

#max 500 page
Jewellery_2 =1

#max 100 page
Belts_1 =1

#max 20 page
Belts_2 =1

#max 40 page
Ties=1

#max 20 page
Cuff=1

#max 20 page
Pocket=1

#max 20 page
Caps=1

#max 30 page
Mufflers=1

#max 10 page
Phn_case=1

#max 40 page
Ring=1

#max 50 page
Socks_1 =1

#max 20 page
Socks_2 =1

#max 50 page
Bracelets=1



#Database [header:] #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#

db_nm="myntra_data"+str(rn(0,1000))+".db"

conn = sqlite3.connect(db_nm)
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
print("Your Current Data_Base:",db_nm)
print("\nCollecting Clothings....\n")
gen="men"
for i in range(2):

       for page in range(Clothing):
              url="https://www.myntra.com/"+gen+"-clothings?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"



#Footwear********************************************

print("Collecting Footwear....\n")

gen="men"
for i in range(2):

       for page in range(Footwear):
              url="https://www.myntra.com/"+gen+"-footwear?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"

#watches********************************************

print("Collecting watches....\n")

gen="men"
for i in range(2):

       for page in range(watches):
              url="https://www.myntra.com/"+gen+"-watches?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"

# Wallets*************************************************

print("Collecting Wallets....\n")

gen="men"
for i in range(2):

       for page in range(Wallets):
              url="https://www.myntra.com/"+gen+"-wallets?p="+str(page+1)+"&plaEnabled=false"

              #print(page+1)
              
              process()
       gen="women"


#bags***************************************************

print("Collecting bags/backpacks....\n")

for page in range(bags_1):
       url="https://www.myntra.com/men-bags?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(bags_2):
       url="https://www.myntra.com/women-bags?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()


#Jewellery***********************************************

print("Collecting Jewellery....\n")

for page in range(Jewellery_1):
       url="https://www.myntra.com/men-jewellery?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(Jewellery_2):
       url="https://www.myntra.com/women-jewellery?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()



#Belts***************************************************

print("Collecting Belts....\n")

for page in range(Belts_1):
       url="https://www.myntra.com/men-belts?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(Belts_2):
       url="https://www.myntra.com/women-belts?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()


#Ties**************************************************

print("Collecting Ties....\n")

for page in range(Ties):
       url="https://www.myntra.com/men-ties?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1): #only 1 page
       url="https://www.myntra.com/ties-girls"

       #print(page+1)
              
       process()

# Cufflinks*******************************************

print("Collecting Cufflinks....\n")

for page in range(Cuff):
       url="https://www.myntra.com/men-cufflinks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1): #only 1 page
       url="https://www.myntra.com/cufflinks-women?p=1&plaEnabled=false"

       #print(page+1)
              
       process()

#Pocket Squares****************************************

print("Collecting Pocket-Squares....\n")

for page in range(Pocket):
       url="https://www.myntra.com/pocket-squares-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

#Caps and Hats********************************************

print("Collecting Caps-and-Hats....\n")

for page in range(Caps):
       url="https://www.myntra.com/caps-for-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(1): #only 1 page
       url="https://www.myntra.com/hats-for-men?p=1&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(2): #max 2 page
       url="https://www.myntra.com/hats-for-women?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

#Mufflers, Scarves and Gloves*******************************

print("Collecting Mufflers, Scarves and Gloves....\n")

for page in range(Mufflers):
       url="https://www.myntra.com/mufflers,-scarves-and-gloves?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

# Phones Cases***********************************************

print("Collecting Phones Cases....\n")

for page in range(Phn_case):  #max 10 page

       url="https://www.myntra.com/phones-cases?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

#Rings and Wristwear*****************************************

print("Collecting Rings and Wristwear....\n")

for page in range(2):  #max 3 page 
       url="https://www.myntra.com/rings-and-wristwear-men?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(Ring): #max 40 page

       url="https://www.myntra.com/rings-and-wristwear-women?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

# Socks***********************************************************  

print("Collecting Socks....\n")

for page in range(Socks_1): #max 50 page
       url="https://www.myntra.com/men-socks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(Socks_2): #max 20 page
       url="https://www.myntra.com/women-socks?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

# Bracelets**********************************************************

print("Collecting Bracelets....\n")

for page in range(3):  #max 10 page
       url="https://www.myntra.com/men-bracelets?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

for page in range(Bracelets): #max 50 page
       url="https://www.myntra.com/women-bracelets?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()

# Chains**********************************************************

print("Collecting Chains....\n")

for page in range(1): #max 3 page
       url="https://www.myntra.com/men-chains?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()


for page in range(2): #max 6 page

       url="https://www.myntra.com/women-chains?p="+str(page+1)+"&plaEnabled=false"

       #print(page+1)
              
       process()


#Database[ending] #*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#**#*#

#close database connection
conn.close()


