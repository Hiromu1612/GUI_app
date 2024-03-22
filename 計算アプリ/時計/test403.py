import datetime
now=datetime.datetime.now()
print(f"現在時刻{now:%Y年%m月%d日 %A %H時%M分%S秒}")

goal=now.replace(hour=20,minute=15,second=0)
print(f"目標時刻{goal:%Y年%m月%d日 %A %H時%M分%S秒}")
td=goal-now
print(f"目標時刻まであと{td}")