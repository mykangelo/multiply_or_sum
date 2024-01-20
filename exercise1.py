


#create function for the calculation of the two number
def multiply_add(first_num, second_num):
    product = first_num * second_num  #store the product of the two number in product 
    if product <= 1000: #create condition if the product is less than or equal to 1000
        print("The answer is", product) #then print the product
    else:
        sum = first_num + second_num #if the total is greater than 1000,
        print("The answer is", sum) #then print the sum 

#store and call the function for the two numbers of the different given
answer1 = multiply_add(20, 30)
answer2 = multiply_add(40, 30)