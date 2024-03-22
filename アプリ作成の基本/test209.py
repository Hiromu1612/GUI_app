import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.Text("1行1列")],sg.Text("1行2列"),sg.Text("1行3列"),
        [sg.Text("2行1列"),sg.Text("2行2列"),sg.Text("2行3列")],
        [sg.Text("3行1列"),sg.Text("3行2列"),sg.Button("ボタン",key="btn")]]
window=sg.Window("要素レイアウトテスト",layout,font=(None,14),size=(300,300))

def execute():
    print("ボタンが押されました")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn":
        execute()

window.close()