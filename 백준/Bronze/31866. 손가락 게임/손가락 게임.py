js, ji = map(int, input().split())

js_chk = js not in [0, 2, 5]
ji_chk = ji not in [0, 2, 5]

if [js_chk, ji_chk] == [True, False] or [js, ji] in [[2, 0], [5, 2], [0, 5]]:
    print('<')

elif [js_chk, ji_chk] == [False, True] or [js, ji] in [[0, 2], [2, 5], [5, 0]]:
    print('>')

else:
    print('=')