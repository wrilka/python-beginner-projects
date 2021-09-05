import math

def area_calc(height, width, coverage):
	area= height * width
	num_can= math.ceil(area / coverage)
	print(f"You need {num_can} Cans")


fill_h = int(input("Input the height of the wall\n"))
fill_w= int(input("Input the width of the wall\n"))
fill_c= float(input("input the coverage per can\n"))

area_calc(height=fill_h, width=fill_w, coverage=fill_c)