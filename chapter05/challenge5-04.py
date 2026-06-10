yuusuke = {"好きなアーティスト":"米津"}

a = input("何を聞きますか:")
if a in yuusuke:
    b = yuusuke[a]
    print(b)
else:
    print("見つかりません")

