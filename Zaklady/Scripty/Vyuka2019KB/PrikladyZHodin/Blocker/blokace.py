website_list=[radek.strip() for radek in open("blokace.txt", "r")]

print(website_list)

wbsite_list2=[]
for web in website_list:
	wbsite_list2.append(web)
	wbsite_list2.append(web[4:])

print(wbsite_list2)