with open("times.txt") as f:
    content = f.readlines()

data = []
for str in content:
	ok = 1
	for i in str:
		if (i == ':' or (i >= '0' and i <= '9') or i == '\n'):
			a = 0
		else:
			ok = 0
	if ok == 1  and str != '\n':
		data.append(str)

final = []

def check(a, b):
	x, y = a.split(":")
	res1 = int(x) * 60 + int(y)
	z, w = b.split(":")
	res2 = int(z) * 60 + int(w)
	if (abs(res1 - res2) <= 1):
		return True
	return False
for i in range(len(data) - 3):
	if (check(data[i], data[i + 1]) or check(data[i], data[i + 2]) or check(data[i], data[i + 3]) or check(data[i], final[len(final) - 1])):
		final.append(data[i])


def check1(a, b):
	x, y = a.split(":")
	res1 = int(x) * 60 + int(y)
	z, w = b.split(":")
	res2 = int(z) * 60 + int(w)
	if (abs(res1 - res2) <= 5):
		return True
	return False

used = [0] * len(final)
cnt = 1
j = 0
for j in range(len(final) - 1):
	if (check1(final[j], final[j + 1])):
		used[j] = cnt
		used[j + 1] = cnt
	else:
		cnt = cnt + 1 
first = [0] * (cnt + 1)
second = [0] * (cnt + 1)
for i in range(len(final)):
	second[used[i]] = i
	if (first[used[i]] == 0):
		first[used[i]] = i
def check2(a, b):
	x, y = a.split(":")
	res1 = int(x) * 60 + int(y)
	z, w = b.split(":")
	res2 = int(z) * 60 + int(w)
	if (abs(res1 - res2) <= 2):
		return True
	return False
def check3(a, b):
	x, y = a.split(":")
	res1 = int(x) * 60 + int(y)
	z, w = b.split(":")
	res2 = int(z) * 60 + int(w)
	return res1 >= res2
def check4(a, b):
	x, y = a.split(":")
	res1 = int(x) * 60 + int(y)
	z, w = b.split(":")
	res2 = int(z) * 60 + int(w)
	if (res1 <= 120 and res2 <= 120):
		return True
	if (res2 < res1):
		return False
	return True
for i in range(1, cnt + 1):
	if (check4(final[first[i]], final[second[i]]) and 
		check2(final[first[i]], final[second[i]]) == False and 
		check3(final[first[i]], final[first[i - 1]])):
		print (final[first[i]] + final[second[i]])
#print final