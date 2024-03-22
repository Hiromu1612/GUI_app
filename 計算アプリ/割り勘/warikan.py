import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.Text("金額と人数を入力してください")],
        [sg.Text("金額"),sg.Input(key="price")],
        [sg.Text("人数"),sg.Input(key="people")],
        [sg.Button("計算",key="calc"),sg.Text(key="txt")]]

window=sg.Window("割り勘アプリ",layout,size=(300,200))

def execute(values):
    #金額と人数を取得 int()で文字列を数値に変換
    price=int(values["price"])
    people=int(values["people"])
    warikan=price/people
    window["txt"].update(f"1人あたり{warikan:.3f}円です")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="calc":
        execute(values)

window.close()