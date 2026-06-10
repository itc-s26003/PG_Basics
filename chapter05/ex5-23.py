lists = []
rap = ["カニエ・ウェスト", "ジェイ・z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
# print(list[0])と同じ
print(lists)
raps = lists[0]
print(raps)   # list[0]はrapのリスト全部   
rap.append("ケンドリック・ラマー")
print(raps)
print(lists)

