import datetime
schedule = [["1時限目",8,30],
            ["昼休み",12,00]]
now = datetime.datetime.now()
now=now.replace(hour=10)
print(f"現在時刻{now:%H時%M分%S秒}")
for s in schedule:
    print(f"{s[0]}まであと{s[1]-now.hour}時間{s[1]-now.minute}分")
