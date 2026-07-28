def string_test(s):
	d = {"UPPER CASE": 0, "LOWER CASE": 0}
	for c in s:
		if c.isupper():
			d["UPPER CASE"] += 1
		elif c.islower():
			d["LOWER CASE"] += 1
		else:
			pass
	print("Original String:", s)
	print("No. of upper case characters:", d["UPPER CASE"])
	print("No. of lower case characters:", d["LOWER CASE"])

string_test("Welcome To Python")
