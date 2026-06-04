def f(a):
    a = a / 2
    return a 
    """
    関数名:f
    引数:a  データ型:int
    戻り値:a / 2
    """
def fd(a):
    a = a * 4
    return a
    """
    関数名:fd
    引数:a  データ型:int
    戻り値:a * 4

    """
a = input("数字を入力:")
b = f(int(a))
c = fd(b)
print(c)
