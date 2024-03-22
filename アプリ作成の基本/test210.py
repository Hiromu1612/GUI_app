import PySimpleGUI as sg
sg.theme("DarkBrown3")

#size=(横,縦)
layout=[[sg.Text("ABCDE",size=(30,1),justification="left")],
        [sg.Text("FGHIJ",size=(30,1),justification="center")],
        [sg.Input("KLMNO",size=(30,1),justification="right")]]

window=sg.Window("テキストの配置テスト",layout,font=(None,14),size=(300,300))
event,values=window.read()
window.close()