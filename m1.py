# import tkinter module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import other necessary modules
import random
import time
import datetime
 
# creating root object
root = Tk()
 
# defining size of window
root.geometry("1200x6000")
root.configure(bg='burlywood1')
 
# setting up the title of window
root.title("Message Encoding and Decoding")
 
Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side=TOP)
 
f1 = Frame(root, width = 800, height = 700,
                            relief = SUNKEN)
f1.pack(side=LEFT)
f1.configure(bg='burlywood1')

 
# ==============================================
#                  TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))
 
lblInfo = Label(Tops, font = ('Georgia', 50, 'bold'),
          text = "SECRET MESSAGING",
                     fg = "Black", bd = 10, anchor='w',bg='burlywood1')
                      
lblInfo.grid(row = 0, column = 0)
 
lblInfo = Label(Tops, font=('Arial Rounded MT Bold', 20, 'bold'),
             text = localtime, fg = "Steel Blue",
                           bd = 10, anchor = 'w')
                         
lblInfo.grid(row = 1, column = 0)
 
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
 
# exit function
def qExit():
    root.destroy()
 
# Function to reset the window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
 
 
# reference
lblReference = Label(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
                text = "Enter your Name:", bd = 16, anchor = "w",bg='burlywood1')
                 
lblReference.grid(row = 0, column = 0)
 
txtReference = Entry(f1, font = ('arial', 16, 'bold'),
               textvariable = rand, bd = 10, insertwidth = 4,
                        bg = "light blue", justify = 'right')
                         
txtReference.grid(row = 0, column = 1)
 
# labels
lblMsg = Label(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
         text = "Enter any MESSAGE", bd = 16, anchor = "w",bg='burlywood1')
          
lblMsg.grid(row = 1, column = 0)
 
txtMsg = Entry(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
         textvariable = Msg, bd = 10, insertwidth = 4,
                bg = "powder blue", justify = 'right')
                 
txtMsg.grid(row = 1, column = 1)
 
lblkey = Label(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
            text = "KEY(pwd)", bd = 16, anchor = "w",bg='burlywood1')
             
lblkey.grid(row = 2, column = 0)
 
txtkey = Entry(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
         textvariable = key, bd = 10, insertwidth = 4,
                bg = "powder blue", justify = 'right')
                 
txtkey.grid(row = 2, column = 1) 
#def show():
   # mode=click.get()
lblmode = Label(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
          text = "Choose any MODE",
                                bd = 16, anchor = "w",bg='burlywood1')
                                 
lblmode.grid(row = 3, column = 0)

def selected(choice):
    choice=click.get()
txtmode=["e for encoding","d for decoding"] 
click=StringVar()
click.set("--Select--")
drop=OptionMenu(f1,click,*txtmode,command=selected)
drop.grid(row=3,column=1)
 


   
lblService = Label(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),text = "The Result-", bd = 16, anchor = "w",bg='burlywood1') 
lblService.grid(row = 2, column = 2)
 
txtService = Entry(f1, font = ('Arial Rounded MT Bold', 16, 'bold'),
             textvariable = Result, bd = 10, insertwidth = 4,
                       bg = "powder blue", justify = 'left')
                        
txtService.grid(row = 2, column = 3)
 
# Vigenère cipher
import base64
 
# Function to encode
def encode(key, clear):
    enc = []
     
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)
                      
        enc.append(enc_c) 
        
         
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()  

# Function to decode
def decode(key, enc):
    dec = [] 
    enc = base64.urlsafe_b64decode(enc).decode()
    
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256)
                            
        dec.append(dec_c)
       
       
        
    return "".join(dec)
def Ref():
    print("Message= ", (Msg.get()))
 
    clear = Msg.get()
    k = key.get()
    #m = txtmode.get()
    choice=click.get()
    if (choice == txtmode[0]):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))


 #enc
# btnenc = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
#                         font = ('arial', 16, 'bold'), width = 10,
#                        text = "Encode", bg = "powder blue",
#                          command = Ref).grid(row =3 , column = 1) 
# #dec
# btndec= Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
#                         font = ('arial', 16, 'bold'), width = 10,
#                        text = "Decode", bg = "powder blue",
#                          command = Ref).grid(row =3 , column = 2)      
# Show message button
def onClick():
    messagebox.showinfo("The Result is","")
    Ref()
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
                        font = ('Arial Rounded MT Bold', 16, 'bold'), width = 10,
                       text = "Show Message", bg = "powder blue",
                         command = onClick).grid(row = 7, column = 1)
#messagebox.showinfo("result", "is")
# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
                  fg = "black", font = ('Arial Rounded MT Bold', 16, 'bold'),
                    width = 10, text = "Reset", bg = "green",
                   command = Reset).grid(row = 7, column = 2)
 
# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
                 fg = "black", font = ('Arial Rounded MT Bold', 16, 'bold'),
                      width = 10, text = "Exit", bg = "Darkolivegreen",
                  command = qExit).grid(row = 7, column = 3)

 
# keeps window alive
root.mainloop()