import PySimpleGUI as sg

#ファイル選択ダイアログファイルの表示 パス付のファイル名を取得
loadname=sg.popup_get_file("テキストファイルを選択してください")
print(loadname)