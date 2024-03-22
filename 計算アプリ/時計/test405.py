import PySimpleGUI as sg
import datetime

layout=[[sg.Text("0.5秒ごとにカウントアップします")],
        [sg.Text(font=("Arial",30),justification="center",size=(20,1),key="txt")]]

#keep_on_top=Trueで常に手前に表示
window=sg.Window("カウントアップ",layout,font=(None,14),keep_on_top=True)
time=0
while True:
    #timeout=500msで0.5秒ごとにイベントを取得
    event,values=window.read(timeout=500)

    time=time+1
    window["txt"].update(f"{time}")
    if event==sg.WIN_CLOSED:
        break
window.close()