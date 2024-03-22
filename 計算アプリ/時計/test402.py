import datetime
start=datetime.datetime.now()
#inputはプログラムを一時停止する関数
input("エンターキーを押して一時停止")
stop=datetime.datetime.now()
print(stop-start)