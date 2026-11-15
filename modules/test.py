# 이미지 표시 테스트
from tkinter import *
import os
window = Tk()

canvas = Canvas(window, width = 500, height = 300)
canvas.pack()

img = PhotoImage(file = os.path.join(os.path.dirname(__file__), "..", "images", "b001.png"))
canvas.create_image(20, 20, anchor = NW, image = img)

window.mainloop()