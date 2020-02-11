import tkinter, requests, json
from PIL import Image, ImageTk
from io import BytesIO

def getImage(url, name):
    response = requests.get(url)
    imagedata = response.content
    window = tkinter.Tk()
    img = Image.open(BytesIO(imagedata))

    canvas = tkinter.Canvas(window, width = img.width, height = img.height)
    canvas.pack()
    image = ImageTk.PhotoImage(image = img)
    canvas.create_image(0, 0, image=image, anchor=tkinter.NW)
    window.mainloop()

def getUrl(url):
    response = requests.get(url)
    p = response.json()
    for r in p['results']:
        getImage(r['image'], r['name'])
getUrl('https://rickandmortyapi.com/api/character/?name=rick&status=alive')