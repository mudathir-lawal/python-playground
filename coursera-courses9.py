def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  # ordered_list1 = [ (list1[(len(list1)- 1)- i]) for i, student in enumerate(list1) ]
  list1.reverse()
  for stud in list1:
    list2.append( stud ) 
  return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))

#####
def highlight_word(sentence, word):
	return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#######
