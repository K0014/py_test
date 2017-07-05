list1 = []
list2 = []

rec = int(raw_input("How many records you want to insert?:"))

print "Please enter %s records with Name and Age:" % (rec)

while rec > 0:
	name = raw_input("Enter Name:")
	list1.append(name)
	age = int(raw_input("Enter Age for %s: " % (name)))
	list2.append(age)
	rec = rec - 1

age_list = []
name_list = []

while list2:
    min_element = list2[0]   
    for i in list2: 
        if i < min_element:
            min_element = i
    	k = list2.index(min_element)
    age_list.append(min_element)
    name_list.append(list1[k])
    list2.remove(min_element)
    list1.remove(list1[k])    


final = zip(age_list, name_list)

print "After sorting in reverse order of age"
print "----------------------"
print "Name", " "*5, "Age"
print "----------------------"
for i in final[::-1]:
	print i[1],
	print " "*5,i[0]