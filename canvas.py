from Tkinter import *

class App:
  def __init__(self,master):
    master.title('Python Canvas Testing')
    master.minsize(width=550, height=450)
    
    settingscanvas = Canvas(master, bg="yellow")
    settingscanvas.pack(side='top',anchor='nw',expand=True,fill='x')
    
    datacanvas = Canvas(master,bd=1,bg="green")
    datacanvas.pack(side='top',anchor='nw'expand=True,fill='both')
    
    for r in xrange(15)
      Label(datacanvas, text='Label 2').grid()
 
 window = Tk()
 
 app = App(window)
 
 mainloop()
 
