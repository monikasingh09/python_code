#! /usr/bin/python


import math


random_no = 0 #variable that holds the actual random number
iteration = 0
count_random_generated = 0 #variable to count the random number generated
probability_higher_value = 0 #variable which denotes the actual number to generated within 2nd half of range
probability_lower_value = 0  #variable which denotes the actual number to generated within 1st half of range


#function to generate count of random numbers to be generated in 1st half and 2nd half range
def generate_higher_and_lower_probability(count_of_random_no):
    global probability_higher_value
    global probability_lower_value
    probability_higher_value = 0.73 * count_of_random_no
    probability_lower_value = 0.23 * count_of_random_no
    if probability_higher_value.split('.')[1] > probability_lower_value.split('.')[1]:
        probability_higher_value = math.ceil(probability_higher_value)
        probability_lower_value = count_of_random_no - probability_higher_value
    else:
        probability_lower_value = math.ceil(probability_lower_value)
        probability_higher_value = count_of_random_no - probability_lower_value



#function to check that random number lies in which half of range
def check_random_no(start, end, number):
    global probability_lower_value
    global probability_higher_value
    mid = int((end - start + 1) /2)
    status = False
    if ((number in range(start, mid + 1)) and (probability_lower_value > 0)):
        probability_lower_value -= 1
        status = True
    elif ((number in range(mid + 1, end + 1)) and(probability_higher_value > 0)):
        probability_higher_value -= 1
        status = True
    return status


#function to generate a random number
def generate_random(start, end):
    global random_no
    global iteration
    iteration += 1
    random_no += iteration
    if random_no > end:
        random_no = random_no%end



#funtion to generate random numbers based on tha count of random numbers passed as the argument and start and end of range
def generate_random_no(start, end, count_of_random_no):
    global count_random_generated
    global random_no
    global iteration
    while (count_random_generated < count_of_random_no):
        generate_random(start, end)
        status = check_random_no(start, end, random_no)
        if not status:
            iteration -= 1
            continue
        else:
            print random_no
            count_random_generated += 1


#get user input for range of numbers to be generated 
random_range = raw_input("please enter the range of random number : ")
#get user input for the count of random numbers to be generated
count_of_random_no = int(raw_input("please enter the count you want to generate random number : "))


#extract start and end from user's range input
random_range = random_range.split('-')
start = int(random_range[0])
end = int(random_range[1])


#generate actual count of random numbers in 2 halves of range
generate_higher_and_lower_probability(count_of_random_no)


#genarate random numbers
generate_random_no(start, end, count_of_random_no)


