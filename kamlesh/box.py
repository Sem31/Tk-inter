from tkinter import *

#that is the function for save given data by user in particular user.txt file
def save_data():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info,lastname_info,age_info)

    file = open("user.json",'w')
    file.write(firstname_info)
    file.write(lastname_info)
    file.write(age_info)
    print("user ",firstname_info," Save data successfully in user.json file")

    firstname_data.delete(0, END)
    lastname_data.delete(0, END)
    age_data.delete(0, END)


#it is for the frame
screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")

# it's define the name of the Labels
firstname_text = Label(text="FirstName ",)
firstname_text.place(x=10,y=60)
lastname_text = Label(text="LastName ",)
lastname_text.place(x=10,y=120)
age_text = Label(text="Age ",)
age_text.place(x=10,y=180)

# set the data type of our data
firstname = StringVar()
lastname = StringVar()
age = IntVar()

#now make the Input fields of each data
firstname_data = Entry(textvariable = firstname,width = "30")
firstname_data.place(x=10,y=100)
lastname_data = Entry(textvariable = lastname,width = "30")
lastname_data.place(x=10,y=150)
age_data = Entry(textvariable = age,width = "30")
age_data.place(x=10,y=210)

# now make button to  save data in particular file
# thats why we make the one def function in the head of the program
# and call by the button you can see it this : "command = save_data"
save = Button(text="SAVE",width="10",height="1",command=save_data)
save.place(x=5,y=250)













