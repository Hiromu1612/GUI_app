a=12
b=1234567
#3桁ごとにカンマ区切り
print(f"a={a:,} b={b:,}")
#ゼロ埋め
print(f"a={a:05} b={b:05}")

c=123.4
d=123.456789
#小数点以下3桁まで
print(f"c={c:.3f} d={d:.3f}")
print(f"c={c:.5f} d={d:.5f}")