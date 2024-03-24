# import tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import detection

# import PIL module
from PIL import Image, ImageTk


xpad = 5
ypad = 5

def analyze(filePath):
    # analyze the given image and report the inferences and confidence levels
    #result = detection.infer(filePath)
    #inference = detection.parse(result)
    inference = 'replace this'
    confidence = '0.85'

    # create and position inference label
    inference = ('Inference: ' + inference)
    l1 = Label(master, text=inference)
    l1.grid(row=0, column=0, padx=xpad, pady=ypad, sticky=NW)

    # create and position confidence label
    confidence = ('Confidence: ' + confidence)
    l2 = Label(master, text=confidence)
    l2.grid(row=0, column=1, padx=xpad, pady=ypad, sticky=N)


# creating main tkinter window/toplevel
master = Tk()
master.title("MRI Detector")

# select and image from the file explorer
filePath = askopenfilename()
image = Image.open(filePath)
photo = ImageTk.PhotoImage(image)
l3 = Label(image=photo)
l3.image = photo

# analyze the given image
analyze(filePath)

# position the image
l3.grid(row=1, column=0, padx=xpad, pady=ypad, columnspan=3, sticky=EW)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
