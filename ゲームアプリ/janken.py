import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout=[[sg.Text("じゃんけんゲーム",size=(30,1),justification="center")],
        [sg.Image("ゲームアプリ/futaba0.png",key="face"),sg.Image(key="hand")],
        [sg.Text(key="text")],
        [sg.Button("グー",key="btn_gu"),sg.Button("チョキ",key="btn_choki"),sg.Button("パー",key="btn_pa")]]

window=sg.Window("じゃんけんゲーム",layout,font=(None,14),size=(600,600))

handing=["ゲームアプリ/h0.png","ゲームアプリ/h1.png","ゲームアプリ/h2.png"]
message=["あいこ","あなたの勝ち","あなたの負け"]
facing=["ゲームアプリ/futaba0.png","ゲームアプリ/futaba1.png","ゲームアプリ/futaba2.png"]

def janken(mynum):
    comnum=random.randint(0,2)
    window["hand"].update(handing[comnum])
    hantei=(comnum-mynum)%3
    window["face"].update(facing[hantei])
    window["text"].update(message[hantei])

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn_gu":
        janken(0)
    if event=="btn_choki":
        janken(1)
    if event=="btn_pa":
        janken(2)

window.close()