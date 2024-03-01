from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

my_img_1 = ImageTk.PhotoImage(Image.open("images/d1.jpg"))
my_img_2 = ImageTk.PhotoImage(Image.open("images/d2.jpg"))
my_img_3 = ImageTk.PhotoImage(Image.open("images/d3.jpg"))
my_img_4 = ImageTk.PhotoImage(Image.open("images/d4.jpg"))
my_img_5 = ImageTk.PhotoImage(Image.open("images/d5.jpg"))

my_images = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

my_label_1 = Label(root, image=my_img_1)
my_label_1.grid(row=0, column=0, columnspan=3)

img_num = 1

def btn_forw():
    global img_num
    if img_num == 1:
        prev_btn.config(state=DISABLED)
    img_num += 1
    if img_num > len(my_images):
        img_num = 1
    update_display()
    prev_btn.config(state=NORMAL if img_num > 1 else DISABLED)
    forw_btn.config(state=NORMAL if img_num < len(my_images) else DISABLED)

def btn_prev():
    global img_num
    if img_num == len(my_images):
        forw_btn.config(state=DISABLED)
    img_num -= 1
    if img_num < 1:
        img_num = len(my_images)
    update_display()
    prev_btn.config(state=NORMAL if img_num > 1 else DISABLED)
    forw_btn.config(state=NORMAL if img_num < len(my_images) else DISABLED)

def update_display():
    my_label_1.configure(image=my_images[img_num - 1])
    img_num_label.config(text=f"Image {img_num}/{len(my_images)}")

prev_btn = Button(root, text="<<", command=btn_prev, state=DISABLED)
exit_btn = Button(root, text="Exit app", command=root.quit)
forw_btn = Button(root, text=">>", command=btn_forw)

prev_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forw_btn.grid(row=1, column=2)

img_num_label = Label(root, text=f"Image {img_num}/{len(my_images)}")
img_num_label.grid(row=2, column=0, columnspan=3)

slideshow_running = False

def start_stop_slideshow():
    global slideshow_running
    if not slideshow_running:
        start_slideshow_btn.config(text="Stop Slideshow")
        slideshow_running = True
        start_slideshow()
    else:
        start_slideshow_btn.config(text="Start Slideshow")
        slideshow_running = False

start_slideshow_btn = Button(root, text="Start Slideshow", command=start_stop_slideshow)
start_slideshow_btn.grid(row=3, column=0, columnspan=3)

def start_slideshow():
    btn_forw()
    root.after(1000, lambda: start_slideshow() if slideshow_running else None)

root.mainloop()
