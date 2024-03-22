from pathlib import Path
import chardet  

#階層を一番上にするとエラー消えた
def loadtext(filename):
    with open(filename, "rb") as f:
        b = f.read()
        enc = chardet.detect(b)["encoding"]
        p = Path(filename)
        txt = p.read_text(encoding = enc)
        print(f"{filename} : {txt}")
loadtext("ファイル操作アプリ/読込・書込・保存/utest.txt") 
loadtext("ファイル操作アプリ/読込・書込・保存/stest.txt") 