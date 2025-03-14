string1 = input("Enter the first string")
string2 = input("Enter the second string")

print("Both strings are equal?:", string1 == string2)
print("Both strings are different?:", string1 != string2)
print("First string is lexicographically greater?:", string1 > string2)
print("Second string is lexicographically greater?", string2 > string1)
print("Are both strings aren equal after lowercasing?:", string1.lower() == string2.lower())