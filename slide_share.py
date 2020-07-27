import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import shutil

slideshareurl=input("enter slideshare url")
filename=input("enter file name")



response=requests.get(slideshareurl)

soup=BeautifulSoup(response.text,"html.parser")

images=soup.find_all('img')
j=0
for image in images:
	temp_url=image.get('data-full') 
	j=j+1

	if temp_url!=None:
		response=requests.get(temp_url,stream=True)
		file=open(filename+str(j)+".jpeg","wb")
		shutil.copyfileobj(response.raw,file)
		del response
		




		
	
