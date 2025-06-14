#1.
fruits = ["appel","cherry","kiwi","banana","mango"]
print(fruits[0:5:4])


#2.
cites = input("Enter 3 cites you recently visited :  ")
a = cites.split()
print(list(a))


#3.
prices  = [1200, 850, 950, 720]
print(prices[:3])


#4.
even = [2,4,6,8,10]
even.append(12)
print(even)


#5.
a =  ['Java', 'C++', 'Go']
a.insert(1,"python")
print(a)


#6.
sentence= input("Enter a sentence : ")
a = sentence.split()
print(a)


#7.
months = ['Jan', 'Feb', 'Mar', 'Apr']
months.pop()
print(months)


#8.
list = ['car', 'bus', 'train']
list.sort()
print(list)
list.reverse()
print(list)


#9.
list = ['apple', 'banana', 'apple', 'cherry']
print(list.count("apple"))


#10.
a = 3
b = 5
print("Tom has {} apples and {} bananas".format(a,b))


#11.
word =['Hello']
print(list(word))


#12.
a = [8,6,4]
b = sum(a)
c= b/3
print(f"sum of 3 integers {b}")
print(f"average of 3 integers {c}")


#13.
name = input('enter ypur name : ')
b = list(name)
print(b)
b.reverse()
print(b)


#14.
names = ['Alice', 'Bob', 'Charlie']
a = "Bob" in names
print(a)


#15
list = ['one', 'two', 'three']
list.clear()
print(list)