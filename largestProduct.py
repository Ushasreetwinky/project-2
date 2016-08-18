
'''
https://projecteuler.net/problem=8
'''
# -*- coding: utf-8 -*-
#takes thirteen digit input and returns multiplication of individuals
def multiple(input1):
    res=1;
    input2=str(input1)
    for ch in input2:
        res=res*int(ch);
    return res;
#reads 1000digit number from a file into a string object
f=open('input','r')
data=f.read();
i=0;
result=0;
number=0;
#intializing the number of digits that needs to have highest product value
x=13;
#loop that traverses for adjacent 13 digits
while i<len(data)-x:
    largestNumber=data[i:i+x];
    if(result<multiple(largestNumber)):
        number=largestNumber;
        result=multiple(largestNumber);
    '''if the digit after 13 digited number is greater than the first digit in 
        13 digited number it takes off first digit and adds next digit else 
        takes off first two digits and adds next two'''
    if(data[i]<=data[i+x]):
        i+=1;
    else:
        i+=2;
#printing the thirteen digit which has highest product value
print("thirteen digits:",number)
#printing product value
print("Greatest product of thirteen adjacent digits:",result)
    
        
