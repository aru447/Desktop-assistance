  
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

hostsFile_path = r"C:\Windows\System32\drivers\etc\hosts"
localhost = "127.0.0.1"

def Response():
    result = myText.get()
    displayText.configure(state='normal')
    displayText.insert(END, result + ",")
    displayText.configure(state='disabled')
    User_Input.delete(0,END)
    

def getSiteFromTextAndBlock():
    global sites
    sites = [x.strip() for x in displayText.get("1.0",END).split(',')] 
    try:        
        with open(hostsFile_path,"r+") as file:
                content = file.read()
                for site in sites:
                    if site in content:
                        pass
                    else:
                        file.write( "\n" + localhost + " " + site)
                mb.showinfo(title="info",message = "all sites blocked ☺")
    except:
        mb.showinfo(title="Exception",message ="Error (⌣́_⌣̀)  ")
        
def unblockAll():
    with open(hostsFile_path,"r+") as file:
            contents = file.readlines()
            file.seek(0)
            for content in contents:
                if not any(website in content for website in sites):
                    file.write(content)
            file.truncate()
            displayText.configure(state='normal')
            displayText.delete('1.0', END)
            displayText.configure(state='disabled')
            mb.showinfo(title="unblock websites", message="Done ☺")

window = Tk()
window.title("WebSite-Blocker")
window.geometry("400x500")

myText = StringVar()
window.resizable(False, False)

User_Input = Entry(window, textvariable=myText, width=50)
User_Input.place(x=40, y=370)
addButton = Button(window, text="Add to list", command=Response, bg="green", height=2, width=10)
addButton.place(x =250, y=420)
blockButton = Button(window, text="Block site", command=getSiteFromTextAndBlock, bg="red", height=2, width=10, )
blockButton.place(x =150, y=420)
unblockButton = Button(window, text="Unblock site", command=unblockAll, bg="blue", height=2, width=10)
unblockButton.place(x =50, y=420)
displayText = Text(window, height=20, width=40)
displayText.pack()
displayText.configure(state='disabled')

window.mainloop()