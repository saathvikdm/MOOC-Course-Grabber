
# coding: utf-8

# In[106]:


from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pandas as pd  
import os
class MyWindow:
    
    csvCheck = 0
    check = 0
    allok = 0
    
    chapters = ""
    unitsList = ""
    links = ""
    totalLength = 0
    sel_path = ""
    
    def __init__(self, win):     
        self.lbl1=Label(win, text="MOOC Course Grabber Tool", height = 2, width = 25,fg='red',bg='black', font=("Helvetica", 16))
        self.lbl1.place(x=0, y=0)
        
        self.lbl4=Label(win, text="Ver 1.0", height = 0, width = 5, font=("Helvetica", 7))
        self.lbl4.place(x=265, y=45)
        
        self.button1 = tk.Button(win, text='Select .csv', command=self.selCsv)
        self.button1.place(x=15, y=100)
        
        self.lbl2text = tk.StringVar()
        self.lbl2text.set("(CSV File Name)")
        self.lbl2=Label(win, textvariable=self.lbl2text, fg='black', font=("Helvetica", 10))
        self.lbl2.place(x=120, y=102)
        
        self.button2=Button(win, text="Set Destination", fg='black', command=self.selDest)
        self.button2.place(x=15, y=150)
        
        self.lbl3text = tk.StringVar()
        self.lbl3text.set("(Destination)")
        self.lbl3=Label(win, textvariable=self.lbl3text, fg='black', font=("Helvetica", 10))
        self.lbl3.place(x=120, y=150)
        
        
        self.lbl4text = tk.StringVar()
        self.lbl4text.set("(Status: Program Started)")
        self.lbl4=Label(win, textvariable=self.lbl4text, fg='grey', font=("Helvetica", 8))
        self.lbl4.place(x=12, y=200)
        
        self.button3=Button(win, fg='BLACK', text="GRAB", bg='GREEN',width = 17, font=("Helvetica", 20)
                           , command = self.grabProcess)
        self.button3.place(x=9, y=250)
        
        self.button4=Button(win, fg='BLACK', text="EXIT", bg='RED',width = 39, command=win.destroy)
        self.button4.place(x=8, y=320)
        
    def selCsv(self):
        sel_csv = filedialog.askopenfilename()
        if(str(sel_csv).split(".")[-1].lower() == "csv"):
            MyWindow.csvCheck = 1
            if(MyWindow.csvCheck == 1):
                col_list = ["CName","UName","URL"]
                df = pd.read_csv(sel_csv, usecols=col_list)
                MyWindow.chapters = df.CName.astype(str)
                MyWindow.unitsList = df.UName.astype(str).tolist()
                MyWindow.links = df.URL.astype(str).tolist()
                MyWindow.totalLength = len(MyWindow.chapters)
                self.lbl2text.set((sel_csv.split("/")[-1]))
                MyWindow.check = 1
                self.lbl4text.set("(Status: File Selected.)")
        elif(MyWindow.csvCheck == 0):
            self.lbl4text.set("(Status: Select a .csv file)")
            print("Select a .csv file")
        
    def selDest(self):
        if(MyWindow.check==1):
            while(1):
                try:
                    course_name = str(self.lbl2text.get().split(".")[0])
                    MyWindow.sel_path = filedialog.askdirectory()+"/"+course_name+"/"
                    os.mkdir(MyWindow.sel_path)
                    self.lbl3text.set("Folder " +MyWindow.sel_path.split("/")[-2]+" Created.")
                    self.lbl4text.set("(Status: Successfully created.)")
                    MyWindow.allok = 1
                    return(0)
                except:
                    MyWindow.error=1
                    self.lbl3text.set("(Destination)")
                    self.lbl4text.set("(Status: Error : Folder Exists/Could Not Create Directory.)")
                    print("Error : Folder Exists or Could Not Create Directory.")
                    return(1)
                else:
                    MyWindow.error=1
                    self.lbl3text.set("(Destination)")
                    self.lbl4text.set("(Status: Error : Error Occured.)")
                    print("Error Occured. Restart Program and try again.")
                    return(1)
        elif(MyWindow.check==0):
            self.lbl4text.set("(Status: Select .csv file first.)")
    
    def grabProcess(self):
        if(MyWindow.allok == 1):
            i = 0
            count = 0;
            while i<MyWindow.totalLength:
                if int(MyWindow.chapters[i][0])==4:    #As '2' is a number that is unique to the index places of the chapters numberings.
                    count = count+1           #counting the number of units in the course
                i = i+1

            list = []
            k = 0
            j = 1
            arr = [0]
            list.append(MyWindow.unitsList[0])
            while k<MyWindow.totalLength:
                if str(MyWindow.unitsList[k]) == str(MyWindow.unitsList[j]):
                    k += 1
                    if j==MyWindow.totalLength-1:
                        j = MyWindow.totalLength-1
                    else:
                        j += 1
                    #print("Working")
                elif str(MyWindow.unitsList[k]) != str(MyWindow.unitsList[j]):
                    list.append(MyWindow.unitsList[j])
                    arr.append(k)
                    k += 1
                    if j==MyWindow.totalLength-1:
                        j = MyWindow.totalLength-1
                    else:
                        j += 1
                    #print("Appended")
                else:
                    #print("Error")
                    break
            arr.append(MyWindow.totalLength) #Adding the last chapter to the length

            path = MyWindow.sel_path
            j = 0
            z = 0
            while j<count:
                try: 
                    final = path+str(j+1)+" - "+list[j].split(' (')[0]+"\\"
                    download = final+list[j].split(' (')[0]+".txt"
                    os.mkdir (final)
                    f = open(download, "w+")
                    for x in MyWindow.links[arr[z]+1:arr[z+1]+1]:
                        f.write(x+"\n")
                    f.close()
                    z = z+1
                    j = j+1
                except OSError:
                    print ("Creation of the directory %s failed" % final)
                else:
                    print ("Successfully created the directory %s " % final)
            dwnload = path + str(1)+" - "+list[0].split(' (')[0] + "\\" + list[0].split(' (')[0] + ".txt"
            f = open(dwnload, "a")
            f.write(MyWindow.links[0])
            f.close()
            self.lbl4text.set("(Status: Grab Finished!)")
            
        elif(MyWindow.allok == 0):
            self.lbl4text.set("(Status: Either file is not selected or Directory is not set.)")

        


        
window=Tk()
mywin=MyWindow(window)
window.resizable(width=False, height=False)
window.title('MOOC Course Grabber Tool')
window.geometry("300x380+10+10")
window.mainloop()

