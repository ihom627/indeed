#!/usr/bin/env python

#Q. Given a list of integers, write a function that returns a list of the product of the other integers in the list for each integer. 
#For example products_of_remaining([2,4,5]) == [20, 10, 8]

def products_of_remaining(list_nums):
	print("initial list_nums[]", list_nums)
	output_list = []
	length = len(list_nums) 
	for index in range (0, length):
		product = 1 
		iter_position = 0
		for iter in list_nums:
			if index != iter_position:
				product	= product * iter
				#print("index!= iter_position, product =", product)
			else:
				next
			iter_position+=1
		#print ("entering value into output_list[] index", index)
		#can't index into unallocated list
		#output_list[index] = product
		output_list.append(product)
	return(output_list) 

def main():
	list_nums_main = [20, 10, 0]
	output_list_nums_main = products_of_remaining(list_nums_main)
	print(output_list_nums_main)

	list_nums_main = [2, 4, 5]
	output_list_nums_main = products_of_remaining(list_nums_main)
	print(output_list_nums_main)

	list_nums_main = [7, 8, 9]
	output_list_nums_main = products_of_remaining(list_nums_main)
	print(output_list_nums_main)



if __name__ == "__main__":
	main()


