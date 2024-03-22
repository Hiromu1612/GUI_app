import random
hand=["グー","チョキ","パー"]
message=["あいこ","あなたの勝ち","あなたの負け"]
mynum=random.randint(0,2)
comnum=random.randint(0,2)
print(f"あなたの手は{hand[mynum]}、コンピュータの手は{hand[comnum]}")
hantei=(comnum-mynum)%3
print(f"{message[hantei]}です")