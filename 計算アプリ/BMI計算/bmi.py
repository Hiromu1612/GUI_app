import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.Text("身長と体重を入力してください")],
        [sg.Text("身長(cm)"),sg.Input(key="height")],
        [sg.Text("体重(kg)"),sg.Input(key="weight")],
        [sg.Button("計算",key="calc"),sg.Text(key="txt")]]

window=sg.Window("BMI計算アプリ",layout,size=(300,200))

def execute(values):
    #身長と体重を取得 int()で文字列を数値に変換
    height=int(values["height"])/100
    weight=int(values["weight"])
    bmi=weight/(height*height)
    if bmi<18.5:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n低体重です")
    elif bmi<25:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n普通体重です")
    elif bmi<30:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n肥満(1度)です")
    elif bmi<35:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n肥満(2度)です")
    elif bmi<40:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n肥満(3度)です")
    else:
        window["txt"].update(f"BMI値は{bmi:.2f}です\n肥満(4度)です")

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="calc":
        execute(values)
window.close()