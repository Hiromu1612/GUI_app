from  pathlib import Path

#ファイルを作成してテキストを書き込む
def savetext(filename):
    p=Path(filename)
    txt="書き出しテスト用のテキストです"
    p.write_text(txt,encoding="utf-8")

savetext("ファイル操作アプリ/読込・書込・保存/output.txt")