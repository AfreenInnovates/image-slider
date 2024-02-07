from tkinter import *
from PIL import ImageTk, Image

# Create the main Tkinter window. root can be named as anything else.
root = Tk()

# storing the images
my_img_1 = ImageTk.PhotoImage(Image.open("d1.jpg"))
my_img_2 = ImageTk.PhotoImage(Image.open("d2.jpg"))
my_img_3 = ImageTk.PhotoImage(Image.open("d3.jpg"))
my_img_4 = ImageTk.PhotoImage(Image.open("d4.jpg"))
my_img_5 = ImageTk.PhotoImage(Image.open("d5.jpg"))

my_images = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

# a label to display the initial image
my_label_1 = Label(root, image=my_img_1)
my_label_1.grid(row=0, column=0, columnspan=3)

# Counter for current image
img_num = 1

# Define a function to handle forward button clicks
def btn_forw():
    global img_num
    if img_num == 1:
        prev_btn.config(state=DISABLED)
    img_num += 1
    if img_num > len(my_images): # checking if we have reached the end of image list
        img_num = 1 # back to image one
    update_display()
    prev_btn.config(state=NORMAL if img_num > 1 else DISABLED)
    forw_btn.config(state=NORMAL if img_num < len(my_images) else DISABLED)


# Define a function to handle previous button clicks
def btn_prev():
    global img_num
    if img_num == len(my_images):
        forw_btn.config(state=DISABLED)
    img_num -= 1
    if img_num < 1: # checking if we have reached the start of image list
        img_num = len(my_images) # reached to last image
    update_display()
    prev_btn.config(state=NORMAL if img_num > 1 else DISABLED)
    forw_btn.config(state=NORMAL if img_num < len(my_images) else DISABLED)


# Update the display based on the current image number
def update_display():
    my_label_1.configure(image=my_images[img_num - 1]) # update image dynamically and more efficient code compared to my_label_1 = Label(root, image=my_images[img_num - 1]) my_label_1.grid(row=0, column=0, columnspan=3)
    img_num_label.config(text=f"Image {img_num}/{len(my_images)}") # same with this line

# Create navigation buttons
prev_btn = Button(root, text="<<", command=btn_prev, state=DISABLED)
exit_btn = Button(root, text="Exit app", command=root.quit)
forw_btn = Button(root, text=">>", command=btn_forw)

# Display navigation buttons on the grid
prev_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forw_btn.grid(row=1, column=2)

# Label to display image counter
img_num_label = Label(root, text=f"Image {img_num}/{len(my_images)}")
img_num_label.grid(row=2, column=0, columnspan=3)

# Slideshow feature
def start_slideshow():
    btn_forw()  # Starts slideshow from current image
    root.after(1000, start_slideshow)  # Change image every 1000 milliseconds (1 second)

start_slideshow_btn = Button(root, text="Start Slideshow", command=start_slideshow)
start_slideshow_btn.grid(row=3, column=0, columnspan=3)

root.mainloop()
