import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout=[[sg.Button("ファイルを開く",key="open")],[sg.Text(key="text")],
        [sg.Button("ファイルを保存",key="save")],
        [sg.Image(key="image")]]

window=sg.Window("モノクロ画像に変換",layout,size=(600,600))

def load_image():
    global image
    loadname=sg.popup_get_file("画像ファイルを選択してください")
    if not loadname:
        return
    try:
        image=Image.open(loadname).convert("L") #モノクロ画像に変換
        image=image.copy()
        image.thumbnail((300,300)) #サムネイル作成 300x300px以下に縮小
        bio=io.BytesIO()
        image.save(bio,format="PNG")
        window["image"].update(data=bio.getvalue())
        window["text"].update(f"{loadname}を表示しました")
    except:
        window["image"].update(data=None)
        window["text"].update(f"{loadname}は画像ファイルではありません")

image=None

def save_image():
    if image==None:
        return
    savename=sg.popup_get_file("画像のファイル名を入力してください",save_as=True)
    if not savename:
        sg.PopupTimed("ファイル名が入力されていません")
        return
    if savename[-4:].lower()!=".png":
        savename+=".png"
    try:
        image.save(savename)
        window["text"].update(f"{savename}に保存しました")
    except:
        window["text"].update(f"{savename}に保存できませんでした")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="open":
        load_image()
    if event=="save":
        save_image()