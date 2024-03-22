import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.Text("入力された年の干支を表示します。")],
        [sg.Text("西暦は何年ですか?"),sg.Input(key="year")],
        [sg.Button("実行",key="btn")],
        [sg.Text("結果表示",key="txt")]]

window=sg.Window("干支計算アプリ",layout,size=(300,200))

def execute(values):
    #int()で文字列を数値に変換
    year=int(values["year"])
    eto_list= ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    eto=eto_list[(year-4)%12]
    window["txt"].update(f"{year}年は{eto}年です")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="btn":
        execute(values)
window.close()