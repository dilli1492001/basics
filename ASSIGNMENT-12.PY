#1. Remove all non-alphabet characters from 'H3ll0_Wor!ld#2025'.
#Expected Output: 'HllWorld'
 
# character = 'H3ll0_Wor!ld#2025'
# for char in character:
#     if char.isalpha():
#         print(char,end = "")


#2. Find the most frequent word in the sentence: 'cat dog dog bird cat cat'.
#Expected Output: 'cat'

# sentence = 'cat dog dog bird cat cat'
# temp = " "
# total = []
# for ch in sentence:
#     if ch.isalpha():
#         temp += ch
#     else:
#         if temp != " ":
#             total.append(temp)
#             temp = " "
# if temp:
#     total.append(temp)






#3. Return the index of the first vowel in the string 'crypt'.
#Expected Output: -1 (no vowels found)

# string = "crypt"
# vowels = "aeiou"
# for j,i in enumerate(string):
#     if i in vowels:
#         print(f"index of first vowel {j}")
#         break
# else :
#     a=vowels.find(i)
#     print(a,"(No vowels found)")



#4. Move all vowels in 'education' to the end while preserving order.
#Expected Output: 'dctneuaio'

# string = "education"
# a=list(string)
# print(a)
# vowels = "aeiou"
# for ch in a:
#     if ch in vowels:
#         a.remove(ch)
#         a.append(ch)
# print(a)




#5. Create a dictionary mapping each character in 'banana' to its frequency.
#Expected Output: {'b':1, 'a':3, 'n':2}

# word = "banana"
# a={}
# count = 0
# for ch in word:
#     if word.count(ch)


    


#6. Replace every vowel in 'hello world' with its uppercase form.
#Expected Output: 'hEllO wOrld'

# word = "hello world"
# vowels ="aeiou"
# for i in word:
#     if i in vowels:
#         i.upper()

#     else:
#         i.lower()
# print(word)




#7. Check if digits in '12345' form a continuous ascending sequence.
#Expected Output: True

# digits = '12354'
# if list(digits) == sorted(digits):
#     print(True)



#8. Count how many words in 'This is a beautiful sunny day' are longer than 4 letters.
#Expected Output: 2
word = "This is a beautiful sunny day"
a = list(word)
print(a,strip())











    









        





    
    

    