from tkinter import *

# GUI
root = Tk()
root.title("Console")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "xin chào"):
		txt.insert(END, "\n" + "Bot -> Tôi có thể giúp gì cho bạn ?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> bạn muốn tôi làm gì ??")

	elif (user == "bạn khoẻ không ?"):
		txt.insert(END, "\n" + "Bot -> tôi ổn! còn bạn ?")

	elif (user == "fine" or user == "tôi khoẻ" or user == "tôi vẫn khoẻ"):
		txt.insert(END, "\n" + "Bot -> tuyệt, tôi có thể giúp gì cho bạn ?")

	elif (user == "cảm ơn" or user == "cảm ơn bạn"):
		txt.insert(END, "\n" + "Bot -> không có gì")

	else:
		txt.insert(END, "\n" + "Bot -> nhắn con cặc j v, t đéo hiểu")

	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Console", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="gửi", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
