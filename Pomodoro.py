import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    timer_title.config(text="Timer", foreground=GREEN)
    window.after_cancel(str(timer))
    timer_title.config()
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_time)
        timer_title.config(text="Break", fg=RED)
    else:
        count_down(short_break_time)
        timer_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if 10 > int(count_sec) > 0:
        count_sec = f"{"0"}{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "️✔️"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

timer_title = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_title.grid(row=0, column=1)

canvas = Canvas(width=360, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 112, image=tomato_img)
timer_text = canvas.create_text(180, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", bg="white", border=0, font=(FONT_NAME, 12, "bold"), padx=5, pady=5, highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

restart_btn = Button(text="Restart", bg="white", border=0, font=(FONT_NAME, 12, "bold"), padx=5, pady=5, highlightthickness=0, command=reset_timer)
restart_btn.grid(row=2, column=2)

check_mark = Label(bg=YELLOW, font=20, foreground=GREEN, pady=20)
check_mark.grid(row=3, column=1)

window.mainloop()
