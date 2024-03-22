import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("DarkBrown3")

layout=[[sg.Button("ファイルを開く",key="open")],sg.Text(key="txt1"),
        [sg.Button("保存",key="save")],
        [sg.Multiline(key="txt2",size=(80,20))]]

#resizable=Trueを指定してウィンドウをリサイズ可能にする
window=sg.Window("テキストファイルの保存",layout,resizable=True)

loadname=None
enc="utf-8"

#ファイルを開く 読み込む
def loadtext():
    #loadnameは別の関数で作った変数の為そのままでは中身が分からないので、Program全体で使えるグローバル変数を使う
    global loadname,enc
    loadname=sg.popup_get_file("ファイルを選択してください")
    if not loadname:
        sg.PopupTimed("キャンセルされました")
        return
    with open(loadname,"rb") as f:
        b=f.read()
        enc=chardet.detect(b)["encoding"]
        p=Path(loadname)
        txt=p.read_text(encoding=enc)
        window["txt1"].update(f"{loadname}は、{enc}です")
        window["txt2"].update(txt)

#ファイルを保存
def savetext():
    global loadname,enc
    savename=sg.popup_get_file("名前を付けて保存",save_as=True)
    #キャンセルされた場合は何もしない
    if not savename:
        sg.PopupTimed("キャンセルされました")
        return
    if savename.find(".")==-1:
        savename+=".txt"
    p=Path(savename)
    p.write_text(window["txt2"].get(),encoding=enc)
    window["txt1"].update(f"{savename}を保存しました")
    loadname=savename

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="open":
        loadtext()
    if event=="save":
        savetext()

window.close()