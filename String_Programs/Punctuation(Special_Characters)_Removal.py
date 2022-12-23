
str=input("Enter String : ")
punc='''!@#$%^&*()_+=-{}0123456789[]:;"'?/<>,.'''
non_punc=""
special_ch=""
for ch in str:
    if ch not in punc:
        non_punc+=ch
    else:
        special_ch+=ch
print("Special Characters present in String are: \n",special_ch)
print("After Removing Special Characters String will be:")
print(non_punc)
