li=[7]

while True:
    a = input("数字を入力：")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("数字か'q'を入力してください")
    

    if a == li[0]:
        print("正解")
    else:
        print("不正解")
