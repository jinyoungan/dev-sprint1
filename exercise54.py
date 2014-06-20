# This is where Exercise 5.4 goes
# Name: Jin

def is_triangle():
	a = int(raw_input("a lenth?\n"))
	b = int(raw_input("b lenth?\n"))
	c = int(raw_input("c lenth?\n"))
	if a > (b + c) or b > (a + c) or c > (a + b) :
		print "No"
	else :
		print "Yes"
is_triangle()

