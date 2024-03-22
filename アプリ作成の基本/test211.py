import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.Text("テキスト",size=(40,1),justification="center")],
        [sg.Input("入力欄")],
        [sg.Multiline("1行目\n2行目",size=(40,5))],
        [sg.Image("futaba.png")]]

window=sg.Window("入力欄テスト",layout,font=(None,14),size=(300,300))
event,values=window.read()
window.close()