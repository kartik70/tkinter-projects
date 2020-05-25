from covid import Covid
import tkinter as tk

covid = Covid()




window = tk.Tk()
window.title("COVID TRACKER")
window.geometry("500x500")
window.configure(background="black")

def show_data():
    tb1.delete(0.0, "end")
    tb2.delete(0.0, "end")
    tb3.delete(0.0, "end")
    tb4.delete(0.0, "end")

    tb1.insert(1.1,"        " + str(covid.get_total_active_cases()))
    tb2.insert(1.1,"        " + str(covid.get_total_confirmed_cases()))
    tb3.insert(1.1, "        " + str(covid.get_total_recovered()))
    tb4.insert(1.1, "        " + str(covid.get_total_deaths()))

def clear():
    tb1.delete(0.0, "end")
    tb2.delete(0.0, "end")
    tb3.delete(0.0, "end")
    tb4.delete(0.0, "end")

t1 = tk.Label(window,text="-------------------------",font =(
  'Verdana'),bg="black",fg="yellow")
t1.pack()
t2 = tk.Label(window,text="LIVE COVID CASES TRACKER",font =(
  'Verdana',25),bg="black",fg="yellow")
t2.pack()
t3 = tk.Label(window,text="-------------------------",font =(
  'Verdana'),bg="black",fg="yellow")
t3.pack()
t4 = tk.Label(window,text="Total Active Cases:",font =(
  'Verdana',15),bg="black",fg="yellow")
t4.pack()

tb1 = tk.Text(window, width = 25, height = 2)
tb1.pack()

t5 = tk.Label(window,text="Total Confirmed Cases:",font =(
  'Verdana',15),bg="black",fg="yellow")
t5.pack()

tb2 = tk.Text(window, width = 25, height = 2)
tb2.pack()

t6 = tk.Label(window,text="Total Recovered Cases:",font =(
  'Verdana',15),bg="black",fg="yellow")
t6.pack()

tb3 = tk.Text(window, width = 25, height = 2)
tb3.pack()

t7 = tk.Label(window,text="Total Deaths:",font =(
  'Verdana',15),bg="black",fg="yellow")
t7.pack()

tb4 = tk.Text(window, width = 25, height = 2)
tb4.pack()

t8 = tk.Label(window,text="-------------------------",font =(
  'Verdana'),bg="black",fg="yellow")
t8.pack()

btn1=tk.Button(window,text="UPDATE",bg="yellow",fg="black",command=show_data)
btn1.pack()

btn2=tk.Button(window,text="CLEAR",bg="yellow",fg="black",command=clear)
btn2.pack()













window.mainloop()