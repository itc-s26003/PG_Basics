qs = ["名前は?",
          "好きな色は?",
          "好きなゲームは?"]
n = 0

while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

