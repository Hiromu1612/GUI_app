import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

layout=[[sg.Text("現在時刻",size=(15,1),justification="center")],
        [sg.Text("0000/00/00(---)",font=("Arial",30),justification="center",size=(20,1),key="txt1")],
        [sg.Text(font=("Arial",30),justification="center",size=(20,1),key="txt2")]]
window=sg.Window("時刻アプリ",layout,font=(None,14),size=(400,200),keep_on_top=True)

def execute():
    now=datetime.datetime.now()
    window["txt1"].update(f"{now:%Y/%m/%d(%a)}")
    window["txt2"].update(f"{now:%H:%M:%S}")

while True:
    event,values=window.read(timeout=1000) #1秒ごとにイベントを取得
    execute()
    if event==sg.WIN_CLOSED:
        break

window.close()