import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout=[[sg.Button("ファイルを開く",key="open")],[sg.Text(key="text")],
        [sg.Image(key="image")]]
window=sg.Window("画像表示",layout,size=(600,600))

def load_image():
    loadname=sg.popup_get_file("画像ファイルを選択してください")
    if not loadname:
        return
    #画像の読み込み 保存
    try:
        image=Image.open(loadname)
        image.thumbnail((300,300)) #サムネイル作成 300x300px以下に縮小
        bio=io.BytesIO() #画像はバイナリーデータだからBytesIOを使う バイナリデータ専用の入れ物
        image.save(bio,format="PNG") #バイナリーデータに変換
        window["image"].update(data=bio.getvalue())
        window["text"].update(f"{loadname}を表示しました")
    except:
        window["image"].update(data=None)
        window["text"].update(f"{loadname}は画像ファイルではありません")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="open":
        load_image()

window.close()