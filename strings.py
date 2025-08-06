""" A string is a sequence of characters. Python treats anything inside quotes as a string. 
This includes letters, numbers, and symbols. """

# 1. String Creation

s1 = 'Python'
s2 = "Coding"
print(s1)
print(s2)

# ------------------------------------------------------------------------------------------------------

# 2. Accessing Characters

s = "PythonIsFun"
print(s[0])   # First character
print(s[4])   # 5th character


# ------------------------------------------------------------------------------------------------------

# 3. Negative Indexing

s = "PythonIsFun"
print(s[-10])  # 3rd character
print(s[-5])   # 5th from end

#------------------------------------------------------------------------------------------------------

# 4. String Slicing

print(s[1:4])   # 'yth'
print(s[:3])    # 'Pyt'
print(s[3:])    # 'honIsFun'
print(s[::-1])  # Reverse string

#------------------------------------------------------------------------------------------------------

# 5. String Immutability

s = "CythonIsFun"
# s[0] = 'R'  # ❌ 
s = "P" + s[1:]  # ✅
print(s)

#------------------------------------------------------------------------------------------------------

# 6. Deleting String

s = "PythonIsFun"
print(s)
del s
# print(s)  # ❌ Will raise NameError if uncommented
print("Deleted 's'")


#------------------------------------------------------------------------------------------------------

# 7. Updating String

s = "i hate Python"

# Updating by creating a new string
s1 = "I" + s[1:]

# replacnig "geeks" with "GeeksforGeeks"
s3 = s.replace("hate", "love")
print(s1)
print(s3)

#------------------------------------------------------------------------------------------------------

# 8. String Methods

s = "I'm a Python developer"
print(len(s))
print(s.upper())
print(s.lower())

s = "   happy coding   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))

#------------------------------------------------------------------------------------------------------

# 9. Concatenation and Repetition
print("Concatenation and Repetition:")
s1 = "Hello"
s2 = "Python"
s3 = s1 + " " + s2
print(s3)

s = "Developer "
print(s * 3)

#------------------------------------------------------------------------------------------------------

# 10. Formatting Strings

name = "Christin"
age = 19
print(f"Name: {name}, Age: {age}")

# Using format method
s = "My name is {} and I am {} years old.".format("Christin", 19)
print(s)

#------------------------------------------------------------------------------------------------------

# 11. Membership Testing
""" The "in" keyword checks if a particular substring is present in a string. """

s = "Python is fun"
print("Python" in s)  # True
print("Java" in s)    # False





