import PySimpleGUI as sg
import random
sg.theme('DarkBrown3')

layout=[[sg.Text("おみくじ",size=(30,1),justification="center")],
        [sg.Image(filename="ゲームアプリ/futaba0.png")],
        [sg.Text(key="txt",size=(30,1),justification="center")],
        [sg.Button("おみくじを引く",key="btn")]]

window=sg.Window("おみくじ",layout,font=(None,14),size=(300,300))

def omikuji():
    kuji=["大吉","中吉","小吉","末吉","凶"]
    kekka=random.choice(kuji)
    window["txt"].update(f"結果は{kekka}です")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn":
        omikuji()

window.close()