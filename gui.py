import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")


#Draw the title
#tkinter.Entry(window).grid(row = 1, column = 0)

title = tkinter.Label(window,text="O's and X's").grid(row = 1,column = 0)





#Draw the grid
tkinter.Button(window,text = "x").grid(row = 0)
tkinter.Button(window,text = "x").grid(row = 0)
tkinter.Button(window,text = "x").grid(row = 0)





        

window.mainloop()