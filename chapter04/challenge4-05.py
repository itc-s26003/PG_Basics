def f(x):
    try:
        x = float(x)
        return x
    except (ValueError):
        print("数字”を”入力")

    """
    関数名:f
    引数:x  データ型:int
    戻り値:x を整数型に
    """




a = input("数字を入力:")
b = f(a)
print(b)
