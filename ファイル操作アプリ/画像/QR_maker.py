import PySimpleGUI as sg
import io
import qrcode
sg.theme("DarkBrown3")

layout=[[sg.Text("URL:")],[sg.Input(key="input")],
        [sg.Button("QRコード作成",key="make")],
        [sg.Button("保存",key="save"),sg.Text(key="text")],
        [sg.Image(key="image")]]

window=sg.Window("QRコード作成",layout,size=(400,400))

image=None

def execute():
    global image #save_image関数でも使うため、グローバル変数にする
    if not vars["input"]:#varsはvaluesの別名
        sg.PopupTimed("URLを入力してください")
        return
    image=qrcode.make(vars["input"]) #qrcode.make()でQRコードを作成
    image.thumbnail((300,300))
    bio=io.BytesIO()
    image.save(bio,format="PNG")
    window["image"].update(data=bio.getvalue())

def save_image():
    if image==None:
        return
    savename=sg.popup_get_file("ファイル名を入力してください",save_as=True)
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
    event,vars=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="make":
        execute()
    if event=="save":
        save_image()

window.close()