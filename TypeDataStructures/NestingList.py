def nest_to_list(nest,aList):

    for element in nest:

        if isinstance(element, str):
            aList.append(element);
        elif isinstance(element, list):
            nest_to_list(element, aList)

    return aList;



c = ['ccc','ddd']

b = ['bb', c, 'ee', 'ff']

h = ['hh', 'ii']

x = ['a', b, 'g', h, 'j']

print("*** NESTING LIST ***")
print( x)
print("-"*50)

print("*** NESTING LIST ***")
final_list = []
nest_to_list(x, final_list)
print (final_list)
print("-"*50)

