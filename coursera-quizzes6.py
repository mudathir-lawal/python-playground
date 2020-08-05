

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [] 

for i, filename in enumerate(filenames):
  if filename.endswith('hpp'):  
    n = len(filename) - 2
    newfilenames.append(filename[:n])
    print('{}, {}, {}'.format(i, n, filename))
  else:
    newfilenames.append(filename)
    print('{}, {}, {}'.format(i, '-', filename))

print('{} {}'.format('\n', filenames))    
print('{} {}'.format('\n', newfilenames))  
print('\n\n')

###
def guest_list(guests):
	for index, guest in enumerate(guests):
		guest_name, age, occupation = guests[index]
		print('{} is {} years old and works as {}'.format(guest_name, age, occupation))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""