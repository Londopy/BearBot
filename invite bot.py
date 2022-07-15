from tkinter import *
import webbrowser

# define an instance of tkinter
tk = Tk()

#  size of the window where we show our website
tk.geometry("800x450")


webbrowser.open("https://discord.com/api/oauth2/authorize?client_id=996582463499423895&permissions=8&scope=bot")