import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
class student:
    def __init__(self,code1,name1,family1):
        self.code1=code1
        self.name1=name1
        self.family1=family1

    def show(self):
        print('code=',self.code1)
        print('name=',self.name1)
        print('family=',self.family1)

class teacher:
    def __init__(self,code2,name2,family2):
        self.code2=code2
        self.name2=name2
        self.family2=family2

    def show(self):
        print('code=',self.code2)
        print('name=',self.name2)
        print('family=',self.family2)

class lesson:
    def __init__(self,code3,name3):
        self.code3=code3
        self.name3=name3


    def show(self):
        print('code=',self.code3)
        print('name=',self.name3)

class marks():
    def __init__(self,code4,name4,name5,name6,family3,mark):
        self.code4=code4
        self.name4=name4
        self.name5=name5
        self.name6=name6
        self.family3=family3
        self.mark=mark

    def show(self):
        print('marks=',self.mark)
        print('code=', self.code4)
        print('name=', self.name4)
        print('name=', self.name5)
        print('name=', self.name6)
        print('family=', self.family3)
        print('family=', self.family4)






from tkinter import *
master=Tk()
leftframe=Frame(master)
leftframe.pack(side = LEFT)
leftframe2=Frame(master)
leftframe2.pack(side = LEFT)
rightframe=Frame(master)
rightframe.pack(side=RIGHT)
rightframe2=Frame(master)
rightframe2.pack(side=RIGHT)



Label(leftframe, text='کد دانشجو').grid(row=0)
Label(leftframe, text='نام دانشجو').grid(row=1)
Label(leftframe, text='نام خانوادگی دانشجو').grid(row=2)
e1=Entry(leftframe)
e2=Entry(leftframe)
e3=Entry(leftframe)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

Label(leftframe2, text='کد دروس').grid(row=0)
Label(leftframe2, text='نام درس').grid(row=1)
Label(leftframe2, text='نام استاد').grid(row=2)
Label(leftframe2, text='نام دانشجو').grid(row=3)
Label(leftframe2, text='نام خانوادگی دانشجو').grid(row=4)
Label(leftframe2, text='نمرات').grid(row=5)
e4=Entry(leftframe2)
e5=Entry(leftframe2)
e6=Entry(leftframe2)
e7=Entry(leftframe2)
e8=Entry(leftframe2)
e9=Entry(leftframe2)
e4.grid(row=0,column=1)
e5.grid(row=1,column=1)
e6.grid(row=2,column=1)
e7.grid(row=3,column=1)
e8.grid(row=4,column=1)
e9.grid(row=5,column=1)


Label(rightframe, text='کد استاد').grid(row=0)
Label(rightframe, text='نام استاد').grid(row=1)
Label(rightframe, text='نام خانوادگی استاد').grid(row=2)
e10=Entry(rightframe)
e11=Entry(rightframe)
e12=Entry(rightframe)
e10.grid(row=0,column=1)
e11.grid(row=1,column=1)
e12.grid(row=2,column=1)


Label(rightframe2, text='کد درس').grid(row=0)
Label(rightframe2, text='نام درس').grid(row=1)
e13=Entry(rightframe2)
e14=Entry(rightframe2)
e13.grid(row=0,column=1)
e14.grid(row=1,column=1)


List_stud=[]
def show_stud_List():
    for i in List_stud:
        i.show()
def stud():
    x_code = int(e1.get())
    x_name = e2.get()
    x_family = e3.get()
    c1=student(x_code,x_name,x_family)
    List_stud.append(c1)



List_marks=[]
def show_marks_List():
    for i in List_marks:
        i.show()
def marks():
    z_code = int(e4.get())
    z_name1 = e5.get()
    z_name2 = e6.get()
    z_name3 = e7.get()
    z_family = e8.get()
    z_mark = int(e9.get())
    d1=marks(z_code,z_name1,z_name2,z_name3,z_family,z_mark)
    List_marks.append(d1)




List_teach=[]
def show_teach_List():
    for i in List_teach:
        i.show()
def teach():
    z_code = int(e10.get())
    z_name = e11.get()
    z_family = e12.get()
    t1=teacher(z_code,z_name,z_family)
    List_teach.append(t1)


List_lessons=[]
def show_lessons_List():
    for i in List_lessons:
        i.show()
def lessons():
    e_code = int(e13.get())
    e_name = e14.get()
    p1=lesson(e_code,e_name)
    List_lessons.append(p1)





addstdbutton=Button(leftframe, text='ثبت',fg='red',command=stud)
addstdbutton.grid(row=4,column=1)

showbutton=Button(leftframe, text='فرم ثبت دانشجو',fg='teal',command=show_stud_List)
showbutton.grid(row=5,column=1)


addmarkbutton=Button(leftframe2, text='ثبت',fg='red',command=marks)
addmarkbutton.grid(row=6,column=1)

showwbbutton=Button(leftframe2,text='فرم ثبت نمرات',fg='teal',command=show_marks_List)
showwbbutton.grid(row=7,column=1)


adddbutton=Button(rightframe, text='ثبت',fg='red',command=teach)
adddbutton.grid(row=8,column=1)

showbbutton=Button(rightframe,text='فرم ثبت استاد',fg='teal',command=show_teach_List)
showbbutton.grid(row=9,column=1)



addlessonbutton=Button(rightframe2, text='ثبت',fg='red',command=lessons)
addlessonbutton.grid(row=10,column=1)

showbbbbutton=Button(rightframe2,text='فرم ثبت دروس',fg='teal',command=show_lessons_List)
showbbbbutton.grid(row=11,column=1)





def printformstudent():
    print(show_stud_List())
button_1=Button(master, text='فرم ثبت دانشجو',fg='purple',command=printformstudent)
button_1.pack()

def printformteacher():
    print(show_teach_List())
button_2=Button(master, text='فرم ثبت استاد',fg='purple',command=printformteacher)
button_2.pack()

def printformsmarks():
    print(show_marks_List())
button_3=Button(master, text='فرم ثبت نمرات',fg='purple',command=printformsmarks)
button_3.pack()

def printformlesson():
    print(show_lessons_List())
button_4=Button(master, text='فرم ثبت دروس',fg='purple',command=printformlesson)
button_4.pack()

def printformreport():
    print(show_marks_List(),show_stud_List(),show_lessons_List(),show_teach_List())
button_5=Button(master, text='ذخیره فایل گزارش',fg='navyblue',command=printformreport)
button_5.pack()


mainloop()