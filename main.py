from tkinter import*
import tkinter as tk
import pandas as pd
import numpy as np
from model import model,scaler

def fun():
    lis1=[]
    a1=pregnancies.get()
    a2=glucose.get()
    a3=bloodPressure.get()
    a4=skinThickness.get()
    a5=insulin.get()
    a6=bmi.get()
    a7=diabetesPedigreeFunction.get()
    a8=age.get()

    lis1.append(a1)
    lis1.append(a2)
    lis1.append(a3)
    lis1.append(a4)
    lis1.append(a5)
    lis1.append(a6)
    lis1.append(a7)
    lis1.append(a8)
    
    
    
    
    ind=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    test_x1 = pd.DataFrame(lis1,index=ind)
    test_x1 = scaler.transform(np.array(test_x1).reshape(1,8))
    prediction=model.predict(test_x1)

    print(prediction)
   
    if prediction==0:
        cv.create_text(750,550,text='NEGATIVE',font= ('arial', 14, 'bold'),fill='blue',anchor='nw',tags=('label'))
    else:
        cv.create_text(750,550,text='POSITIVE',font= ('arial', 14, 'bold'),fill='green',anchor='nw',tags=('label'))
        
def reset():
    pregnancies.set("")
    glucose.set("")
    bloodPressure.set("")
    skinThickness.set("")
    insulin.set("")
    bmi.set("")
    diabetesPedigreeFunction.set("")
    age.set("")
    cv.delete('label')


root = tk.Tk()
root.title('DIABETICS ANALSIS AND PREDICTION')
root.geometry("1260x660")
root.resizable(0, 0)

menu1=Menu(root)
root.config(menu=menu1)

fileMenu=Menu(menu1)  
menu1.add_cascade(label="FILE",menu=fileMenu)
fileMenu.add_command(label="Reset",command=reset)      
fileMenu.add_command(label="Exit",command=root.destroy)

graphMenu=Menu(menu1)
menu1.add_cascade(label="GRAPH ANALYSIS",menu=graphMenu)                    
graphMenu.add_command(label="Heatmap")

cv = tk.Canvas(width=600, height=600)
cv.pack(side='top', fill='both', expand='yes')

fname ="diabetes.jpg"
bg_image = tk.PhotoImage(file=fname)
cv.create_image(0,0, image=bg_image, anchor='nw')


cv.create_text(400,120, text="Pregnancies",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,160, text="Glucose",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,200, text="BloodPressure",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,240, text="SkinThickness",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,280, text="Insulin",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,320, text="BMI",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,360, text="DiabetesPedigreeFunction",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')
cv.create_text(400,400, text="Age",font=("Helvetica", 15,'bold'),fill="black", anchor='nw')

pregnancies = StringVar()
glucose= StringVar()
bloodPressure= StringVar()
skinThickness= StringVar()
insulin= StringVar()
bmi= StringVar()
diabetesPedigreeFunction= StringVar()
age= StringVar()

entry0=tk.Entry(cv,textvariable = pregnancies, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=120,anchor='nw' )
entry1=tk.Entry(cv,textvariable = glucose, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=160,anchor='nw' )
entry2=tk.Entry(cv,textvariable = bloodPressure, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=200,anchor='nw' )
entry3=tk.Entry(cv,textvariable = skinThickness, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=240,anchor='nw' )
entry4=tk.Entry(cv,textvariable = insulin, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=280,anchor='nw' )
entry5=tk.Entry(cv,textvariable = bmi, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=320,anchor='nw' )
entry6=tk.Entry(cv,textvariable = diabetesPedigreeFunction, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=360,anchor='nw' )
entry7=tk.Entry(cv,textvariable = age, font = ('arial', 14, 'bold'), bd = 8, insertwidth = 4,
                justify = 'left').place(x=650,y=400,anchor='nw' )

btn=tk.Button(cv,text="SHOW RESULT",font=('arial',18,'bold'),command=fun)
btn.place(x=700,y=500,anchor='se')
#button=Button(cv,text = "Show Result", command=fun, padx = 16, pady = 8, bd = 8, fg = "black",
#font = ('arial', 14, 'bold'), width = 12, bg = "aquamarine")
#button.grid(row=8,column=1)

root.mainloop()
