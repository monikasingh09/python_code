
Task 1:
Read file "data.json", and write a recursive function to convert every value of key "quantity" to 23gm, 50gm and 260gm, presently data is given for 100gm.

Algorithm:
1)Load the data from data.json using json.load function.

2)get value for key 'data' from data loaded from json file.

3)get tha value for key '100gm' from data extracted in step 2.

4)write a function quantity conversion which recursively updates value for key 'quantity' of data extracted in step 3.

5)In quantity conversion, check that data is dictionary or not. If it is dictionary then get list of keys of data.If 'quantity' is present in list of keys then  upddate the value using a function.But if 'quantity' is not in list of keys then call quantity conversion function over the value of each key of data. 

6)In quantity conversion,if data extracted in step 3 is not dictionay then call quantity conversion over list of values present in data. 

7)Write an update_data fucntion that updates the value for key 'quantity' for 23gm,50gm and 260gm.

8)generate 23gm,50gm and 260gm equivalent value using a conversion function.

9)conversion takes place in following way:
    23gm_value = 0.23*actual_value
    50gm_value = 0.50*actual_value
    260gm_value = 2.60*actual_value

10)Dump the updated data to data.json using json.dumps()

11) new file is added is pushed as data.json


########################################################################################################################################################################################

Task 2 :
Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want ‘a random number between 1 to 10’ 100 times then it should give ‘number morethan 5’ 73 times and ‘less than 5’ 27 times. You’re not allowed to use any predefined random number generation function nor use of any kind of third party library to generate random number.


Algorithm:
1)Take user input for range of random number and count of random numbers.

2)Get start and end of range given by user

3)Find actual count of random numbers that are to be generated in 2 halves of the range.Divide range in 2 halves.Count of random numbers in 1st half must be equal to 23% of total count of random number and count of random numbers in 2nd half must be equal to 73% of toal count.Convert the count with higher fractional part using math ceiling function and get other count by subtracting the count got by math ceiling from total random count.


4)generate random number x times(given by user).Keep a gloabl variable iteration.For generating a random number define a function that generates a random number by adding a global varibale(first increament this by 1) that is added to previos random number.If random number is greater than end of range then random number is equal to random_no(mod)end of range.

5)After generating random number check that it lies in which half of range and if it lies in any of the range than decrement the count of that range by 1 and return true. But if  random no.  lie in a range for which desired random count has been reached then return false and generate a new random number. 


