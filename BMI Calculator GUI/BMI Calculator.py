from tkinter import *
def bmi():
    bmi= (float(e2.get())*703)/(float(e1.get()))**2
    if bmi<18.5: 
        l = Label(a,text=f"Your BMI value is {round(bmi,2)} (Underweight)")
        l.grid(row=7,pady = 5)
    elif 18.5<=bmi<25:
        l = Label(a,text=f"Your BMI value is {round(bmi,2)} (Normal)")
        l.grid(row=7,pady = 5)
    elif bmi>25:
        l = Label(a,text=f"Your BMI value is {round(bmi,2)} (Overweight)")
        l.grid(row=7,pady = 5)
    else:
        l = Label(a,text="Bmi is not in range")
        l.grid(row=7,pady = 5)
        
a = Tk()
a.title("BMI App")
a.geometry("350x150+500+180")
a.minsize(350,150)
a.maxsize(350,150)
l = Label(a,text = "Enter your height(inches):")
l.grid(row=2,column=0,pady=10,padx=25)
e1 = Entry(a)
e1.grid(row=2, column=2,pady=10)
l = Label(a,text="Enter your weight(pounds):")
l.grid(row =3, column=0,pady=5,padx=25)
e2 = Entry(a)
e2.grid(row=3, column=2,pady=5 )
b = Button(a,text="Find BMI",command= bmi)
b.grid(row=5, column=0)
a.mainloop()
