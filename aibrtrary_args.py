def name(*args):
    for n in args:
        print("Aye", n)
name("Pyae", "Moet", "Bo")


def total(*args):
    sum = 0
    for x in args:
      sum = sum + x
    print(sum)

total(1,2,3)

