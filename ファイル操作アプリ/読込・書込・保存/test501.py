#chardetを使ってファイルの文字コードを判定する
#出来なかった #階層を一番上にするとエラー消えた
import chardet

def loadtext(filename):
    #ファイルの読み込み
    with open(filename,"rb") as f:
        b = f.read()
        enc=chardet.detect(b)["encoding"]
        print(f"{filename}は、{enc}")
loadtext("ファイル操作アプリ/読込・書込・保存/utest.txt")
loadtext("ファイル操作アプリ/読込・書込・保存/stest.txt")