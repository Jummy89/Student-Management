from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import uuid
from tkinter.ttk import Combobox
import mysql.connector
import select
import pathlib


background = "#06283D"
Framebg = "#EDEDED"
Framefg = "#06283D"
root = Tk()
root.title("STUDENT REGISTRATION SYSTEM")
root.geometry("1250x700+50+0")

root.config(bg=background)

#################### Gender ################################
def Selection():
    global gender
    value =radio.get()
    if value==1:
        gender="Male"
    else:
        gender="Female"

###################################################################################
def registration():
    print(str(uuid.uuid4())[0:15])


####################### Save ####################
def Save():
       R1=Registration.get()
       N1=Name.get()
       C1=Class.get()
       try:
           G1=gender
       except:
           messagebox.showerror("error", "Select Gender!")

       D2=DOB.get()
       D1=Date.get()
       G1=radio.get()
       Rel=Religion.get()
       S1=Skill.get()
       fathername=F_Name.get()
       mothername=M_Name.get()
       F1=Father_Occupation.get()
       M1=Mother_Occupation.get()

       if R1=="" or N=="" or C1=="Select Class" or D2=="" or Rel=="" or S1=="" or fathername=="" or mothername=="" or F1=="" or M1=="":
          messagebox.showerror("error","Few data is missing!")
       else:
           con=mysql.connector.connect(host='localhost',user='root',password='',database='Student_data')
           cur=con.cursor()
           cur.execute('Insert into Students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (Registration.get(),
                                                                             Name.get(),
                                                                             Class.get(),
                                                                             DOB.get(),
                                                                             radio.get(),
                                                                             Date.get(),
                                                                             Religion.get(),
                                                                             Skill.get(),
                                                                             F_Name.get(),
                                                                             M_Name.get(),
                                                                             Father_Occupation.get(),
                                                                             Mother_Occupation.get()

                                                                              ))
           try:
               img.save("Student images/" + str(R1) + ".jpg")
           except:
               messagebox.showinfo("info", "profile picture is not available!!!")
           con.commit()
           con.close()
           messagebox.showinfo("Success", "Record has been Inserted")
           Clear()


##################################################################
def Clear():
   global img
   Registration.set(0)
   Name.set('')
   DOB.set('')
   Religion.set('')
   Skill.set('')
   F_Name.set('')
   M_Name.set('')
   Father_Occupation.set('')
   Mother_Occupation.set('')
   Class.set("Select Class")



   saveButton.config(state = 'normal')
   img1=PhotoImage(file='Images/upload photo.png')
   lbl.config(image=img1)
   lbl.image=img1
   img=""
##############################################################################
def Exit():
    root.destroy()
###################### ShowImage ###################################
def Showimage():
      global filename
      global img
      filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",filetype=(
                                                                                 ("JPG File","*.jpg"),
                                                                                 ("PNG File","*.png"),
                                                                                 ("ALL files","*.txt")))
      img = (Image.open(filename))
      resized_image= img.resize((190, 190))
      photo3 = ImageTk.PhotoImage(resized_image)
      lbl.config(image=photo3)
      lbl.image = photo3

################ top frames #######################
Label(root,text="Email: Olajummycomputertechnology@gmail.com",width=10,height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)
Label(root,text="STUDENT REGISTRATION",width=10,height=2,bg="#0000FF",fg='#fff',font='arial 18 bold').pack(side=TOP,fill=X)

################ search box to update ##################
Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=1,font="arial 18").place(x=840,y=70)
photo=PhotoImage(file="Images/search.png")
Srch=Button(root,text="Search",compound=LEFT,image=photo,width=123,bg='#68ddfa',font="arial 13 bold",)
Srch.place(x=1060,y=66)

photo2=PhotoImage(file= "Images/layer.png")
Update_button=Button(root, image=photo2, bg="#c36464")
Update_button.place(x=110,y=64)


################Registration and Date##################
Label(root, text="Registration No:",font="arial 13",fg=Framebg,bg=background).place(x=30,y=150)
Label(root, text="Date",font="arial 13",fg=Framebg,bg=background).place(x=500,y=150)

Registration=IntVar()
Date = StringVar()

reg_entry = Entry(root,textvariable=Registration,width=15,font="arial 12")
reg_entry.place(x=160,y=150)



################## Date #################
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root,textvariable=Date,width=15,font="arial 12")
date_entry.place(x=550,y=150)

Date.set(d1)

################# Student details #################
obj=LabelFrame(root,text="Student Details",font=20,bd=2,width=900,bg=Framebg,fg=Framefg,height=250,relief=GROOVE)
obj.place(x=30,y=200)

Label(obj,text="Full Name:",font="arial 13",bg=Framebg,fg=Framefg).place(x=30,y=50)
Label(obj,text="Date of Birth:",font="arial 13",bg=Framebg,fg=Framefg).place(x=30,y=100)
Label(obj,text="Gender:",font="arial 13",bg=Framebg,fg=Framefg).place(x=30,y=150)

Label(obj,text="Class:",font="arial 13",bg=Framebg,fg=Framefg).place(x=500,y=50)
Label(obj,text="Religion:",font="arial 13",bg=Framebg,fg=Framefg).place(x=500,y=100)
Label(obj,text="Skills:",font="arial 13",bg=Framebg,fg=Framefg).place(x=500,y=150)

Name=StringVar()
name_entry = Entry(obj,textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y=50)

radio= IntVar()
R1 = Radiobutton(obj,text="Male", variable=radio, value=1,bg=Framebg,fg=Framefg, command=Selection)
R1.place(x=150,y=150)

R2 = Radiobutton(obj,text="Female", variable=radio, value=2,bg=Framebg,fg=Framefg, command=Selection)
R2.place(x=200,y=150)

DOB=StringVar()
dob_entry = Entry(obj,textvariable=DOB,width=20,font="arial 10")
dob_entry.place(x=160,y=100)

Religion=StringVar()
religion_entry = Entry(obj,textvariable=Religion,width=20,font="arial 10")
religion_entry.place(x=630,y=100)

Skill=StringVar()
skill_entry = Entry(obj,textvariable=Skill,width=20,font="arial 10")
skill_entry.place(x=630,y=150)


Class= Combobox(obj,values=['1','2','3','4','5','6','7','8','9','10','11','12'],font="Roboto 10",width=17,state="r")
Class.place(x=630,y=50)
Class.set("Select Class")

###################Parents details
obj2=LabelFrame(root,text="Parent Details",font=20,bd=2,width=900,bg=Framebg,fg=Framefg,height=220,relief=GROOVE)
obj2.place(x=30,y=470)

Label(obj2,text="Father's Name:",font="arial 13",bg=Framebg,fg=Framefg).place(x=30,y=50)
Label(obj2,text="Occupation:",font="arial 13",bg=Framebg,fg=Framefg).place(x=30,y=100)

F_Name=StringVar()
f_entry = Entry(obj2,textvariable=F_Name,width=20,font="arial 10")
f_entry.place(x=160,y=50)

Father_Occupation=StringVar()
FO_entry = Entry(obj2,textvariable=Father_Occupation,width=20,font="arial 10")
FO_entry.place(x=160,y=100)

Label(obj2,text="Mother's Name:",font="arial 13",bg=Framebg,fg=Framefg).place(x=500,y=50)
Label(obj2,text="Occupation:",font="arial 13",bg=Framebg,fg=Framefg).place(x=500,y=100)

M_Name=StringVar()
M_entry = Entry(obj2,textvariable=M_Name,width=20,font="arial 10")
M_entry.place(x=630,y=50)

Mother_Occupation=StringVar()
MO_entry = Entry(obj2,textvariable=Mother_Occupation,width=20,font="arial 10")
MO_entry.place(x=630,y=100)

#############image #################
f=Frame(root,bd=3,bg="black",width=200,height=200,relief=GROOVE)
f.place(x=1000,y=150)
img=PhotoImage(file="Images/upload photo1.png")
lbl=Label(root,bg="black",image=img)
lbl.place(x=1000,y=150)

################### button ##############
Button(root,text="Upload",width=19,height=2,font="arial 12 bold",bg="lightblue",command=Showimage).place(x=1000,y=370)
saveButton=Button(root,text="Save",width=19,height=2,font="arial 12 bold",bg="lightgreen",command=Save)
saveButton.place(x=1000,y=450)
Button(root,text="Reset",width=19,height=2,font="arial 12 bold",bg="lightpink",command=Clear).place(x=1000,y=530)
Button(root,text="Exit",width=19,height=2,font="arial 12 bold",bg="red",command=Exit).place(x=1000,y=610)

root.mainloop()
