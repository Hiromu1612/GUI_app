import PySimpleGUI as sg
# レイアウトの作成
layout=[[sg.Text(key="txt")],
        [sg.Button("実行",key="btn")],]
# ウィンドウの作成
window=sg.Window('Simple data entry window',layout,size=(300,100))

def execute():
    window["txt"].update("こんにちは")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn":
        execute()