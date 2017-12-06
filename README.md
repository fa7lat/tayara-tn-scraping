# Overview 

This is a Python Script for web scraping on www.tayara.tn and sending email in html format  with list of items <br>
<ul>
<li>Price</li> 
<li>Image</li>
<li>Phone Number of the contact person</li>
</ul>

# Notes 

```
url = "https://www.tayara.tn/fr/bizerte/toutes_les_categories/"+quote("à_vendre")+"/"+term
```
You can change the searched term , or use the input function
```
term = input('What do you want to search ? :')
```
tayara.tn is using images to display phone number of the contact person , I am using OCR Tesseract to get the number in String format
You can install it from here : <a href="https://github.com/tesseract-ocr/tesseract/wiki"> Tesseract </a>

<b>email library</b> is used to make the email content in HTML format so I can I use the <b>img</b> tag to display the item image.
