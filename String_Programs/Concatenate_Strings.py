'''
#Method1 (Using + operators)
str1="Hello"
str2="World"
conc_str=str1+" "+str2
print(conc_str)

#Method2 (Using join() method)
str1="Hello"
str2="World"
conc_str=" ".join([str1,str2])
print(conc_str)

#Method3 (Using % method)
str1="Hello"
str2="World"
conc_str="%s %s"%(str1,str2)
print(conc_str)

'''
#Method4 (Using format() function)

str1="Hello"
str2="World"
conc_str="{} {}".format(str1,str2)
print(conc_str)