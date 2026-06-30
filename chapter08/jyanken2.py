import random
print("じゃんけん")
print("1:グー,2:チョキ,3:パー")
player = int(input("手を入力してください:"))
rsp = ["","グー","チョキ","パー"]
com = random.randint(1,3)
print("あなたの手：",rsp[player])
print("COMの手",rsp[com])

if player == com:
    print("あいこ")
elif abs(player-com) == 1:
    
    if player < com:
        print("あなたの勝ち")
    else:
        print("あなたの負け")
else:

    if player == 1:
        print("あなたの負け")
    else:
        print("あなたの勝ち")

'''
elif player < com:
    if player+1 == com:
        print("あなたの手",player_hand)
        print("COMの手",com_hand)
        print("あなたの勝ち")
    elif player+2 == com:
        print("あなたの手",player_hand)
        print("COMの手",com_hand)
        print("あなたの負け")

    print("あなたの手",player_hand)
    print("COMの手",com_hand)
    print("あなたの勝ち")
else:
    print("あなたの手",player_hand)
    print("COMの手",com_hand)
    print("あなたの負け")
'''
