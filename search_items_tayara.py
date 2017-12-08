from login_pswd import strFrom, strTo, pswd

import sys

import time

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text  	  import MIMEText
from email.mime.image 	  import MIMEImage
from email.header         import Header    

from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
from urllib.parse import quote  
import requests

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from io import BytesIO  

import pandas as pd
import numpy as np


# Prepare link
 
# term = input('Search : ')

def send_res(term="iPhone-6"):

	#term = term.replace(' ', '-')
	url = "https://www.tayara.tn/fr/bizerte/toutes_les_categories/"+quote("à_vendre")+"/"+term

	# Request and open connection , close once done
	req = Request(url, headers={'User-Agent':'Chrome'})
	page_html = urlopen(req).read()

	# Parse the html page and find all articles with that url 

	page_soup = soup(page_html,"html.parser")
	articles = page_soup.find_all('article')



	# Phone Number Class
	phone_number_class = 'showPhoneNumber mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--yellow mbs'

	# get number from image url
	def get_number(x):
	    phone_image = "https://www.tayara.tn/phone/"+x+"?type=image"
	    response_img = requests.get(phone_image)
	    phone_number = pytesseract.image_to_string(Image.open(BytesIO(response_img.content)), lang = 'eng')
	    return phone_number


	res = []
	for article in articles:
	    if article.find('img') is not None:
	        detail_soup = soup(requests.get(article.a['href']).content, 'html.parser')
	        phone_number_link = detail_soup.find('a',{'class':phone_number_class})['data-on-click']
	        phone_number = get_number(phone_number_link)
	                        
	        img = article.find('img')['data-blazy']
	        price = article.find('span').text.strip()
	        res.append([img, price, phone_number])




	# Create Dataframe from the result  array with columns Image Link and Price
	# Remove space in the price rows and keep only numeric values
	# Change dtype of the column Price to float from object and filter dataframe to keep only price between 100 & 1000


	df = pd.DataFrame(res,columns=['Image Link','Price','Phone Number'])
	df['Price'] = df['Price'].str.replace('\s+','')
	df['Phone Number'] = df['Phone Number'].str.replace('\D+','')

	df = df[df['Price'].apply(lambda x:x.isnumeric())]
	#df ['Price'] = df['Price'].astype(str).astype(float)

	#df = df [(df['Price'] > 100) & (df['Price'] < 1000)]

	# Sending Email 

	now = time.strftime("%c")

	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = term +' Search ' +now
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Create HTML format as content

	texti = ''

	for index , row in df.iterrows():
	    texti += '<div><b>Price</b> '+str(row['Price'])+'  :  <img src='+row['Image Link']+'> <br><b> Phone Number <b> :'+str(row['Phone Number'])+'<br></div>'
	    


	final_text = '<b> Search for'+str(term)+'</b> <br> '+texti
	msgText = MIMEText(texti,'html')
	msgRoot.attach(msgText)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	server.login(strFrom, pswd)
	server.ehlo()
	server.sendmail(strFrom, strTo, msgRoot.as_string())
	server.quit()

if __name__ == "__main__":

	try:
		sys.argv[1]
		term = '-'.join(sys.argv[1:])
	
	except : print(" [*] Hint: python search_items_tayara.py <search term>"); exit(0)
		
	else:
		send_res(term)






