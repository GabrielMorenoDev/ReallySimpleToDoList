import time
import tkinter
from tkinter import ttk

import sv_ttk
def main():
    root = tkinter.Tk()
    #root.geometry("300x100")
    root.resizable(False, True)
    #root.overrideredirect(True)
    root.bind("<Escape>", lambda a: root.destroy())
    topFrame = ttk.Frame(
        root,
        width=300,
        height=20,   
    )
    topFrame.place(x=0,y=0)
    topFrame.pack()

    button = ttk.Button(root, text="Add Task", command= lambda: task_input(root))
    button.pack(pady=20)

    
    # This is where the magic happens
    sv_ttk.set_theme("dark")
    widget_drag_free_bind(root)
    root.mainloop()


def add_task(root, taskInputWindow, textLabel):
    if bool(textLabel.strip()):
        label = ttk.Label(root, text=textLabel, padding=1)
        label.bind("<Button-1>", lambda event: label_destroy(label))
        label.pack()
        taskInputWindow.destroy()
    else:
        task_input(root)
        taskInputWindow.destroy()

def widget_drag_free_bind(widget):
    """Bind any widget or Tk master object with free drag"""
    if isinstance(widget, tkinter.Tk):
        master = widget  # root window
    else:
        master = widget.master

    x, y = 0, 0
    def mouse_motion(event):
        global x, y
        # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
        offset_x, offset_y = event.x - x, event.y - y  
        new_x = master.winfo_x() + offset_x
        new_y = master.winfo_y() + offset_y
        new_geometry = f"+{new_x}+{new_y}"
        master.geometry(new_geometry)

    def mouse_press(event):
        global x, y
        count = time.time()
        x, y = event.x, event.y

    widget.bind("<B1-Motion>", mouse_motion)  # Hold the left mouse button and drag events
    widget.bind("<Button-1>", mouse_press)  # The left mouse button press event, long calculate by only once


def label_destroy(label):
    label.destroy()

def task_input(root):
    window = tkinter.Toplevel(root)
    window.overrideredirect(True)
    window.resizable(False,False)
    
    inputArea = tkinter.StringVar()
   # ttk.Entry(window, name="task description", textvariable=inputArea).pack()
    entry = ttk.Entry(window, name="task description", textvariable=inputArea)
    entry.focus()
    entry.bind("<Return>",lambda event : add_task(root,window,inputArea.get()))
    entry.pack()
    ttk.Button(window, text="insert task", command=lambda: add_task(root,window,inputArea.get())).pack()
    
    
    

if __name__ == '__main__':
    main()


