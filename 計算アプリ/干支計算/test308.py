eto = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
year=2022
etonum = (year - 4) % 12
print(f"{year}年は、{eto[etonum]}年です。")
