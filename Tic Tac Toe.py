a_list = ['a']
b_list = ['b']
c_list = ['c']
d_list = ['d']
e_list = ['e']
f_list = ['f']
g_list = ['g']
h_list = ['h']
i_list = ['i']

print('Player 1 = @')
print('Player 2 = #')

var = 1
while var == 1 :

	print (a_list[0], b_list[0], c_list[0])
	print (d_list[0], e_list[0], f_list[0])
	print (g_list[0], h_list[0], i_list[0])
	z = input('@ Pick a letter: ')

	if z =="a":
		a_list.remove("a")
		a_list.append("@")

	if z =="b":
		b_list.remove("b")
		b_list.append("@")

	if z =="c":
		c_list.remove("c")
		c_list.append("@")

	if z =="d":
		d_list.remove("d")
		d_list.append("@")

	if z =="e":
		e_list.remove("e")
		e_list.append("@")

	if z =="f":
		f_list.remove("f")
		f_list.append("@")

	if z =="g":
		g_list.remove("g")
		g_list.append("@")

	if z =="h":
		h_list.remove("h")
		h_list.append("@")

	if z =="i":
		i_list.remove("i")
		i_list.append("@")

	if (a_list[0]) == ('@'):
		if (b_list[0]) == ('@'):
			if (c_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (d_list[0]) == ('@'):
		if (e_list[0]) == ('@'):
			if (f_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (g_list[0]) == ('@'):
		if (h_list[0]) == ('@'):
			if (i_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (a_list[0]) == ('@'):
		if (d_list[0]) == ('@'):
			if (g_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (b_list[0]) == ('@'):
		if (e_list[0]) == ('@'):
			if (h_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (c_list[0]) == ('@'):
		if (f_list[0]) == ('@'):
			if (i_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (a_list[0]) == ('@'):
		if (e_list[0]) == ('@'):
			if (i_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (c_list[0]) == ('@'):
		if (e_list[0]) == ('@'):
			if (g_list[0]) == ('@'):
				print('@ Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	print (a_list[0], b_list[0], c_list[0])
	print (d_list[0], e_list[0], f_list[0])
	print (g_list[0], h_list[0], i_list[0])
	z = input('# Pick a letter: ')

	if z =="a":
		a_list.remove("a")
		a_list.append("#")

	if z =="b":
		b_list.remove("b")
		b_list.append("#")

	if z =="c":
		c_list.remove("c")
		c_list.append("#")

	if z =="d":
		d_list.remove("d")
		d_list.append("#")

	if z =="e":
		e_list.remove("e")
		e_list.append("#")

	if z =="f":
		f_list.remove("f")
		f_list.append("#")

	if z =="g":
		g_list.remove("g")
		g_list.append("#")

	if z =="h":
		h_list.remove("h")
		h_list.append("#")

	if z =="i":
		i_list.remove("i")
		i_list.append("#")

	if (a_list[0]) == ('#'):
		if (b_list[0]) == ('#'):
			if (c_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (d_list[0]) == ('#'):
		if (e_list[0]) == ('#'):
			if (f_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (g_list[0]) == ('#'):
		if (h_list[0]) == ('#'):
			if (i_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (a_list[0]) == ('#'):
		if (d_list[0]) == ('#'):
			if (g_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (b_list[0]) == ('#'):
		if (e_list[0]) == ('#'):
			if (h_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (c_list[0]) == ('#'):
		if (f_list[0]) == ('#'):
			if (i_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (a_list[0]) == ('#'):
		if (e_list[0]) == ('#'):
			if (i_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break

	if (c_list[0]) == ('#'):
		if (e_list[0]) == ('#'):
			if (g_list[0]) == ('#'):
				print('# Wins')
				print (a_list[0], b_list[0], c_list[0])
				print (d_list[0], e_list[0], f_list[0])
				print (g_list[0], h_list[0], i_list[0])
				break
