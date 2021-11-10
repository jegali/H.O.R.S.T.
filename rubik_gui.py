from tkinter import *
import os

# this is used to pad the GUI
padding = 20

# the size of the facelets...
facelet_size = 60
# ... is used to calculate te window dimensions
canvas_width = 12 * facelet_size + padding
canvas_height = 9 * facelet_size + padding

colorcurrent = None
colorpicker_id = [0 for column in range(6)]

facelet_id = [[[0 for column in range(3)] for row in range(3)] for face in range(6)]
face_name = ("U", "R", "F", "D", "L", "B")
face_colors = ("white", "red", "green", "yellow", "orange", "blue")

offset = ((1,0), (2,1), (1,1), (1,2), (0,1), (3,1))

# create the facelets
def create_facelets(facelet_size):
    for face in range(6):
        for row in range(3):
            y = (row * facelet_size) + (offset[face][1] * facelet_size * 3) + padding / 2    
            for column in range(3):
                x = (column * facelet_size) + (offset[face][0] * facelet_size * 3) +padding / 2
                facelet_id[face][row][column] = canvas.create_rectangle(x,y, (x + facelet_size), (y + facelet_size), fill=face_colors[face])   
                if (row == 1 and column == 1):
                    canvas.create_text(x + facelet_size / 2, y + facelet_size / 2, font=("", 14), text=face_name[face], state=DISABLED)
    for face in range(6):
        canvas.itemconfig(facelet_id[face][1][1], fill=face_colors[face])


# remove the colors from the facelets - except the center pieces
def clear_facelets():
    for face in range(6):
        for row in range(3):
            for column in range(3):
                if row != 1 or column != 1:
                    canvas.itemconfig(facelet_id[face][row][column], fill="grey")


# reset the cube and set it ti solved
def reset_facelets():
    for face in range(6):
        for row in range(3):
            for column in range(3):
                canvas.itemconfig(facelet_id[face][row][column], fill=canvas.itemcget(facelet_id[face][1][1], "fill"))


# create the colorpicker
# via the colorpicker, the user can chose the color and set it to facelets
def create_colorpicker(facelet_size):
    global colorcurrent
    for color in range(6):
        x = 7 * facelet_size + (facelet_size + 5) * (color % 3)
        y = 7 * facelet_size + (facelet_size + 5) * (color // 3)
        colorpicker_id[color] = canvas.create_rectangle(x, y, (x + facelet_size), (y + facelet_size), fill = face_colors[color])
        canvas.itemconfig(colorpicker_id[0], width=4)
    colorcurrent = face_colors[0]

# this method is called if the user clicks the left mouse button on the canvas
def click(event):
    global colorcurrent
    idlist = canvas.find_withtag("current")
    # if the user clicks on an pbject on the canvas, the list has a len of >= 1
    if len(idlist) > 0:
        if idlist[0] in colorpicker_id:
            # save the chosen colorpicker color
            colorcurrent = canvas.itemcget("current", "fill")
            # redraw the picker and the chosen field
            for color in range(6):
                canvas.itemconfig(colorpicker_id[color], width = 1)
            canvas.itemconfig("current", width = 5)    
        else:
            if (idlist[0] != 5 and idlist[0] != 15 and idlist[0] != 25 and idlist[0] != 35 and idlist[0] != 45 and idlist[0] != 55):
                # use the chosen color to fill the clicked facelet
                canvas.itemconfig("current", fill=colorcurrent)


def call_solver():
    os.system("python ../Rubik/rubik.py")
    print("Back in Black")

def call_webcam():
    os.system("python ./webcam.py")
    print("Back in Black")


# create a TkInter window
GUIWindow = Tk()
GUIWindow.title("Cube GUI")

# create a canvas for the windows. 
# We will paint on the canvas
canvas = Canvas(GUIWindow, width=canvas_width, height=canvas_height)
canvas.pack()

# create the gui
# create the facelets
create_facelets(facelet_size)
# create the colorpicker
create_colorpicker(facelet_size)

# create and set the button for clearing the cube 
btn_clear = Button(text="Clear Cube", height=1, width=10, relief=RAISED, command=clear_facelets)
btn_clear_window = canvas.create_window(20,20,anchor=NW, window=btn_clear)

# create and set the button for resetting the cube so solved state 
btn_reset = Button(text="Reset Cube", height=1, width=10, relief=RAISED, command=reset_facelets)
btn_reset_window = canvas.create_window(20,50,anchor=NW, window=btn_reset)

# Call the 3d-solver 
btn_reset = Button(text="Start webcam", height=1, width=10, relief=RAISED, command=call_webcam)
btn_reset_window = canvas.create_window(20,80,anchor=NW, window=btn_reset)

# Call the 3d-solver 
btn_reset = Button(text="Start Solver", height=1, width=10, relief=RAISED, command=call_solver)
btn_reset_window = canvas.create_window(20,110,anchor=NW, window=btn_reset)


# set an event handler for the whole canvas
# if the left mouse button is clicked, call the method click
canvas.bind("<Button-1>", click)

# enter the TkInter event loop
GUIWindow.mainloop()