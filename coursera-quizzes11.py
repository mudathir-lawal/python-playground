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
        if letter not result:
            result[letter] = 0
        result[letter] += 1
    return result    
            
count_letters("Shokolokobangoshe")
