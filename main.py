import math
from tkinter import *
from PIL import Image, ImageTk

work_min = 20
short_break_min = 10
long_break_min = 20
reps = 0
timer= None

# reset timer
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    submit_label.config(text="")
    reps=0


# countdown mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if reps % 8==0:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg="red")

    elif reps % 2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="pink")

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="green")

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions= math.floor(reps/2)
        for i in range(work_sessions):
            marks+= "✔"
        submit_label.config(text= marks)

# UI SETUP
window = Tk()
window.title("WORK & BREAK TIMER")
window.config(padx=5, pady=10, bg="magenta")

canvas = Canvas(width=580, height=550, bg="magenta", highlightthickness=0)
photo = ImageTk.PhotoImage(Image.open("to.png"))
canvas.create_image(270, 290, image=photo)
timer_text = canvas.create_text(290, 300, text="00:00", fill="white", font=("courier", 45, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg="green", bg="magenta", font=("courier", 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="start", font=("courier", 15, "bold"), bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("courier", 15, "bold"), bg="white", command=reset)
reset_button.grid(column=2, row=2)

submit_label = Label(fg="green", bg="magenta", font=("courier", 35, "bold"))
submit_label.grid(column=1, row=3)

window.mainloop()
