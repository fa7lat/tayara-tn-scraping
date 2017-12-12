# Overview 

This is a Python Script for web scraping on www.tayara.tn and sending email in html format  with list of items <br>
<ul>
<li>Price</li>
<li>Phone Number of the contact person</li>
<li>Image</li>
</ul>

# Notes 
URL used for searching : term is the argument to precise when you execute the script via the terminal

```
url = "https://www.tayara.tn/fr/bizerte/toutes_les_categories/"+quote("à_vendre")+"/"+term
```

How to use : (Don't worry about spacing example : Play Station 4)

```
python search_items_tayara.py <search for something>
```

tayara.tn is using images to display phone number of the contact person , I am using OCR Tesseract to get the number in String format , if the number is not available , 00000 would be shown instead.

You can install Tesseract from here : <a href="https://github.com/tesseract-ocr/tesseract/wiki"> Tesseract </a>
Don't forget to mention the installation path for tesseract :

```
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
```

Finally ,Create a file that stores your email crediantals and import it to the main script .
Do Not forget to  add it to gitignore file , among the __pycache__ folder

<img src="https://raw.githubusercontent.com/chemsseddine/tayara-tn-scraping/master/images/Screenshot.PNG">
