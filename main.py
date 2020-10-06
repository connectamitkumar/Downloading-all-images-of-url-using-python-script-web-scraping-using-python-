import requests
import bs4
import shutil
url=input("enter the url:")
response=requests.get(url)
#print(type(response))
#print(response.text)
filename="temp.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")

formatted_text=bs.prettify()
#print(formatted_text)

try:
    with open(filename, "w+") as f:
        f.write(formatted_text)
except Exception as e:
    print(e)

list_imgs=bs.find_all('img')
print(list_imgs)
no_of_imgs=len(list_imgs)
list_as=bs.find_all('a')
no_of_as=len(list_as)
print("number of img tags:",no_of_imgs)
print("number of anchor tags:",no_of_as)

j=1
for imgtag in list_imgs:
    try:
        print(imgtag)
        imglink = imgtag.get('src')
        # print(imglink)
        ext = imglink[imglink.rindex('.'):]
        if ext.startswith('.png'):
            ext='.png'
        if ext.startswith('.jpeg'):
            ext='.jpeg'
        if ext.startswith('.jpg'):
            ext='.jpg'
        if ext.startswith('.svg'):
            ext='.svg'
        filenam = str(j) + ext
        res = requests.get(imglink, stream=True)

        with open(filenam, 'wb') as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as e:
        print(e)
    j=j+1
