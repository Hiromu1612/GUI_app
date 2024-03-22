import tkinter as tk

def execute():
    lb["text"]="こんにちは"

root=tk.Tk()
root.title("こんにちはテスト")
root.geometry("450x350+350+250")

lb=tk.Label(text="")
btn=tk.Button(text="実行",command=execute)

lb.pack()
btn.pack()
root.mainloop()
