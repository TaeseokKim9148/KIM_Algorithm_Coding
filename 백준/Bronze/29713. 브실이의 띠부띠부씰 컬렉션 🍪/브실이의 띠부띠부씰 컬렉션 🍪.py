n = int(input())  
s = input()  


pilyou = {
    'B': 1, 'R': 2, 'O': 1, 'N': 1, 'Z': 1, 
    'E': 2, 'S': 1, 'I': 1, 'L': 1, 'V': 1
}


b_count = s.count('B')
r_count = s.count('R')
o_count = s.count('O')
n_count = s.count('N')
z_count = s.count('Z')
e_count = s.count('E')
s_count = s.count('S')
i_count = s.count('I')
l_count = s.count('L')
v_count = s.count('V')


finsh = min(
    b_count // pilyou['B'],
    r_count // pilyou['R'],
    o_count // pilyou['O'],
    n_count //pilyou['N'],
    z_count // pilyou['Z'],
    e_count // pilyou['E'],
    s_count // pilyou['S'],
    i_count // pilyou['I'],
    l_count // pilyou['L'],
    v_count // pilyou['V']
)


print(finsh)