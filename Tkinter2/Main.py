
import tkinter

clicks = 0


def click_button():
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))

root = tkinter.Tk()
root.title("GUI на Python")
root.geometry("300x250")

buttonText = tkinter.StringVar()
buttonText.set("Clicks {}".format(clicks))

btn = tkinter.Button(textvariable=buttonText, background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()