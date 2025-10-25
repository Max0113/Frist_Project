from tkinter import *

win = Tk()
win.geometry("400x300")

# Text Box
text_box = Text(win, wrap=NONE)
text_box.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar عمودية
scrollbar_y = Scrollbar(win, orient=VERTICAL, command=text_box.yview)
scrollbar_y.pack(side=RIGHT, fill=Y)

# Scrollbar أفقية
scrollbar_x = Scrollbar(win, orient=HORIZONTAL, command=text_box.xview)
scrollbar_x.pack(side=BOTTOM, fill=X)

# ربط text box مع scrollbars
text_box.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)



win.mainloop()



