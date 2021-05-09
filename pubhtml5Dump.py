import requests
import shutil

url = input("Url --> ")
firstPage = int(input("First page --> "))
finalPage = int(input("Final page --> "))
FileDestination = input("File destination for saved images --> ")

for x in range(firstPage, finalPage):

    filename = str(x) + ".jpg"
    imageDestination = fileDestination + "/" + filename
    image_url = url + "/files/large/" + filename

    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
        with open(fileDestination,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ',filename)
        
    else:
        print('Image Couldn\'t be retreived: ', filename)