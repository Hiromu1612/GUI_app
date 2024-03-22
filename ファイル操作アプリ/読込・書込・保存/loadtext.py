import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("Dark Blue 3")

layout=[[sg.Button("ファイルを開く",key="open")],sg.Text(key="txt1"),
        [sg.Multiline(key="txt2",size=(80,20))]]

window=sg.Window("テキストファイル読み込み",layout)

def loadtext():
    global loadname,enc
    loadname=sg.popup_get_file("ファイルを選択してください")
    if not loadname:
        return
    with open(loadname,"rb") as f:
        b=f.read()
    #文字コードを調べる
    enc=chardet.detect(b)["encoding"]
    #ファイルの読み込み
    p=Path(loadname)
    txt=p.read_text(encoding=enc)
    window["txt1"].update(f"{loadname}は、{enc}です")
    window["txt2"].update(txt)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="open":
        loadtext()

window.close()