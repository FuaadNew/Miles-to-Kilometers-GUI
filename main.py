from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
def button_clicked():
    new_text = input.get()
    kmvalue = round(float(new_text) * 1.60934,2)
    my_label4["text"] = kmvalue


my_label1= Label(text= "is equal to",font= ("Ariel",15,))
my_label1.grid(column= 0, row =1)
button = Button()
button = Button(text= "Calculate",command = button_clicked )
button.grid(column= 2, row =3)



input = Entry()
input.grid(column=2,row=0)
my_label2= Label(text= "Miles",font= ("Ariel",15,))
my_label2.grid(column= 3, row =0)

my_label3= Label(text= "Km",font= ("Ariel",15,))
my_label3.grid(column= 3, row =1)

my_label4= Label(text= "0",font= ("Ariel",15,))
my_label4.grid(column= 2, row =1)

#button2 = Button(text= "Click Me",command = button_clicked )
#button2.grid(column=3,row =0)

window.mainloop()