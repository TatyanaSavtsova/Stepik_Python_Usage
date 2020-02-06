with open("test1.txt") as f:
    x = f.readlines()
    x.reverse()
with open("test2.txt", "w") as w:
    w.writelines(x)
