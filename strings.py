#character  frequency counting

#using a dictonary tO count the frequency of characters in a string
def char_frequency_dict(s):
    freq = {}
    for char in freq:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    return freq
text = ""
frequency_dict = char_frequency_dict(text)
print(frequency_dict)

#using dict.get()
def char_frequency_dict(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        return freq
    text = "hello"
frequency_dict_get = char_frequency_dict(text)
print(frequency_dict_get)

#using collection.counter
from collection import counter
def char_frequency_counter(s):
    return dict(counter(s))
text = "hello"
frequency_counter = char_frequency_counter(text)
print(frequency_counter)

#using str.count() method
def char_frequency_counter_method(s):
    freq = {}
    for char in set(s):
        freq[char] = s.count(char):
        return freq
text = "hello"
frequency_count_method = char_frequency_counter_method(text)
print(frequency_count_method) 
