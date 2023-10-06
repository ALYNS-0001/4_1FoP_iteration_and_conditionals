"""
This file is for you to practice slicing strings in - this will be useful for
completing the iteration and conditionals task.
"""

string1 = "abcd efgh ijkl mnop qrst uvwx yz"

#the following is the syntax for slicing into a string for a single letter (or char)

sub_string1 = string1[3]
print(sub_string1)

"""
1.a you try slicing into string1. See if you can get hold of the letters 'a', then 'b', then 'p'
assign your slice to a variable and print that variable out as in the example above
you will need to find the INDEX of the relevant letter in string1 to get hold of it.
"""

# write your code here

"""
1.b if that is working try concatenating the variables holding 'a', 'b' and 'p'
to produce the string 'abp'
"""

#write your code here

"""
2.a now try slicing into a longer portion of the string. slice into string1 to produce a 
variable which holds the value 'mnop'. Look at/unhash and run the example below if you need help"""

#substring2 = string1[5:9]
#print(substring2)


"""
3. A clever trick if you want to slice into a string from the end is to slice using a 
negative index. Unhash the below to see how that works and try it yourself by getting 
the character 'w' from string 1.
"""

#char1 = string1[-1]
#print(char1)


"""
4. Even better is to use the shortcuts for slicing from the beginning to a certain index
OR from an index in the middle to the end. Unhash the below and figure out whats going on
"""

#start_to_middle = string1[:15]
#print(start_to_middle)

#middle_to_end = string1[15:]
#print(middle_to_end)




