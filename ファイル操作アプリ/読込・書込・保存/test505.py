import PySimpleGUI as sg

#ファイル保存ダイアログを表示する
savename=sg.popup_get_file("名前を付けて保存してください",save_as=True)
print(savename)