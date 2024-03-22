import PySimpleGUI as sg

layout=[[sg.Input("フタバ")],
        [sg.Button("実行")],
        [sg.Text("こんにちは")]]
#ウィンドウの作成 "タイトル",部品のリスト 
window=sg.Window("テスト",layout)

#ボタン押しの待機 どのボタンが押されたか,各部品の値を取得
event,values=window.read()
#ボタンが押されたら閉じる
window.close()