'''
#Without numeric Value in list
list=["He","is","Good","Boy"]
lt1=" ".join(list)
print(lt1)
'''
#With numeric value in list..we have to use map() method
list=["He","is",12,"years","old","and","lives","on",32,"A","Street"]
lt1=" ".join(map(str,list))
print(lt1)

