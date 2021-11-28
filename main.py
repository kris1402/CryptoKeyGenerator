import tkinter as tk
import csv
from tkinter import messagebox
from cryptography.fernet import Fernet
from tkinter import filedialog
import Key_Generator


import cryptography

HEIGHT = 500
WIDTH = 600
startIMS = 27099522

mylist = []
mylistIMSI = []
newList = []



def convert_num(strInput):
    return int(strInput)

def split(word):
    return [char for char in word]

def test_function(entry, entry1):
    #print(split(entry))
    n1 = convert_num(entry)
    n2 = convert_num(entry1)
    n3 = n1 - n2
    print("This is the entry:", type(n1))
    print("This is the entry:", type(n2))
    return n3

def split_entry(entry):
    mylist = split(entry)
    mylistIMSI = split(str(startIMS))
    if (len(mylist) == 19):
        #print('Numer ma ' + str(len(mylist)) + ' liczb')
        #print(mylist[12])
        #print(mylistIMSI)
        for i in range(12,19):
            #print(mylist[i])
            mylistIMSI.append(mylist[i])
            #print(newList)
    else:
        tk.messagebox.showinfo(message='Wrong IMSI format!')
    #print(mylistIMSI)
    ######################
    res = int("".join(mylistIMSI))
    return res

'''
def create_csv():
    split_entry(entry.get())
    n4 = convert_num(entry.get())
    #Select directory
    filename = filedialog.askdirectory()
    name = entry2.get()
    print(name)
    #print(filename)
    with open(filename + '/' + name + '.csv', 'w', newline='') as f:
        thewriter = csv.writer(f,delimiter=';')
        for i in range(0,1+(test_function(entry.get(), entry1.get()))):
            n5 = str(n4-i)
            thewriter.writerow([n4-i,split_entry(n5),'64K_M2M_4G_Orange_V2','','0000','0000','10000000','10000000','000000001E197203'])
        tk.messagebox.showinfo(message='File ' + 'mycsv.csv' + ' was generated in ' + filename )
'''

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='#779EC6', bd=5)
frame1.place(relx=0.5, rely=0.32, relwidth=0.75, relheight=0.1, anchor='n')

#File name
'''entry2 = tk.Entry(frame1, font=30)
entry2.place(relx=0.25,relwidth=0.4, relheight=1)'''



lower_frame = tk.Frame(root, bg='#779EC6', bd=10)
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#########################
button2= tk.Button(frame1, text = "Generate", font=40, command=lambda: Key_Generator.test_fun())
button2.place(relx=0.2,relheight=1, relwidth=0.3,anchor = 'n')
button2 = tk.Button(frame1, text="Read Key", font=40, command=lambda: Key_Generator.test_fun_read())
button2.place(relx=0.85, relheight=1, relwidth=0.3,anchor = 'n')
##########################





root.mainloop()