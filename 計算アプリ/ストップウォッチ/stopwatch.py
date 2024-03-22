import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

layout=[[sg.Text("00:00:00",size=(20,1),font=("Helvetica",40),key="time")],
        [sg.Push(),sg.Button("Start/Stop",key="bt"),sg.Push()]]
window=sg.Window("ストップウォッチ",layout,font=(None,14),size=(400,200),keep_on_top=True)

#start_stopボタンが押されたときの処理
def execute():
    if start==True:
        now=datetime.datetime.now()
        td=now-starttime
        window["time"].update(td)

def start_stop():
    global start,starttime
    if start==True:
        start=False
    else:
        start=True
        starttime=datetime.datetime.now()

start=False
while True:
    event,values=window.read(timeout=50)
    execute()
    if event==sg.WIN_CLOSED:
        break
    if event=="bt":
        start_stop()

window.close()