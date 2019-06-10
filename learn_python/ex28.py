# 算False and 1你会得到表达式的第一个操作数(False)	,但是如果你计算True	and	1的时候，你得到它的第二个操作数(1)

list_a = [True and True,
          False and True,
          1 == 1 and 2 == 1,
          "text" == "test",
          1 == 1 or 2 != 1,
          True and 1 == 1,
          False and 0 != 0,
          True or 1 == 1,
          "test" != "testing",
          "test" == 1,
          not (True and False),
          not (1 == 1 and 0 != 1),
          not (10 == 1 or 1000 == 1000),
          not (1 != 10 or 3 == 4),
          not ("testing" == "testing" and "Zed" == "Guy"),
          1 == 1 and (not ("testing" == 1 or 1 == 0)),
          "chuck" == "bacon" and (not (3 == 4 or 3 == 3)),
          3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")),
          ]

for line in list_a:
    print(line)
    print(type(line))
