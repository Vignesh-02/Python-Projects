import requests
from bs4 import BeautifulSoup
import pandas

# link="https://wwww" + ".century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
# r = requests.get(link, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
l=[]
base_url="https://www.century21.com/real-estate/chicago-il/LCILCHICAGO/?pr=%7C20000&p="
for page in range(1,3):
	print(base_url+str(page))
	r=requests.get(base_url+str(page))
	c=r.content
# print(c)
	soup=BeautifulSoup(c,"html.parser")
	all=soup.find_all("div",{"class":"property-card-primary-info"})
# a=all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
# print(a)
# print(len(all))

	for item in all:
		d={}
		try:
			d["Price"]=item.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")
		except:
			d["Price"]=None
		try:
			d["Address"]=item.find("div",{"class":"property-address"}).text.replace("\n","").replace(" ","")
		except:
			d["Address"]=None
		try:
			d["City"]=item.find("div",{"class":"property-city"}).text.replace("\n","").replace(" ","")
		except:
			d["City"]=None
		# j1=j1.find_all("div",{"class":"pdp-info-address"}).text.replace("\n","")
		# j2=j.find_all("div",{"class":"city-state"}).text.replace("\n","")
		
		# print(i,j0,j1)
		# print(i,j1,j2)
		try:
			d["Sqft"]=item.find("div",{"class":"property-sqft"}).find("strong").text
			# print(b)
		except:
			d["Sqft"]=None
		
		try:
			d["Beds"]=item.find("div",{"class":"property-beds"}).find("strong").text
			# print(b1)
		except:
			d["Beds"]=None
		
		try:
			d["Baths"]=item.find("div",{"class":"property-baths"}).find("strong").text
			# print(b2)
		except:
			d["Baths"]=None
		
		l.append(d)


df=pandas.DataFrame(l)
print(df)
df.to_csv("ChicagoBig_Output.csv")


