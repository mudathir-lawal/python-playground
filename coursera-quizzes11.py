def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60 
    return hours, minutes, remaining_seconds
    
result = convert_seconds(5000)
type(result)    


def count_letters(text):
    result = {}
    for letter in text:
        if letter != result:
            result[letter] = 0
        result[letter] += 1
    return result    
            
no_of_chars = count_letters("Shokolokobangoshe")
print(no_of_chars)
print(no_of_chars.values())

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "Red"

violet = Flower()
violet.color = "Purple"

this_pun_is_for_you = "This pun is for you."

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 
