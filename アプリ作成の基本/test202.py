import PySimpleGUI as sg
# レイアウト部分
layout=[[sg.Input("フタバ",key="in")],
        [sg.Button("実行",key="btn")],
        [sg.Text(key="txt")]]
# ウィンドウの作成
window=sg.Window("あいさつテスト",layout)

#実行部分
def execute():
    txt="こんにちは"+values["in"]+"さん"
    window["txt"].update(txt)

while True:
    event,values=window.read()
    if event=="btn":
        execute()
    if event==sg.WIN_CLOSED: #None:でも可
        break
window.close()

#Input=I,Button=B,Text=T, key=k,event=e,values=v,window=winで省略可能