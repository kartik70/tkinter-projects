
import requests, json
from time import sleep
import tkinter

def getBitcoinPrice():
  URL = 'https://www.bitstamp.net/api/ticker/'
  try:
    r = requests.get(URL)
    priceFloat = float(json.loads(r.text)['last'])
    return priceFloat
  except requests.ConnectionError:
    print("Error querying Bitstamp API  ")


window = tkinter.Tk()
window.title("BTC LIVE ALERT")
window.geometry("350x250")
window.configure(background="black")


def show_data():
  text_box.insert(0.0, str(getBitcoinPrice())+" $")

def clear():
  text_box.delete(0.0,"end")




tkinter.Label(window,text="LIVE BITCOIN PRICE !!",bg="black",fg="yellow",width=50,height=5).grid(row=0,column=0)

tkinter.Label(window, text="", bg="black", fg="yellow", width=50).grid(row=2, column=0)

text_box = tkinter.Text(window, width = 25, height = 2)
text_box.grid(row = 1, column = 0, columnspan = 2)

btn1=tkinter.Button(window,text="UPDATE",bg="yellow",fg="black",command=show_data)
btn1.grid(row=3,columnspan=2)

btn2=tkinter.Button(window,text="CLEAR",bg="yellow",fg="black",command=clear)
btn2.grid(row=4,columnspan=2)




window.mainloop()










