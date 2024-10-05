a = (1, 55464, 69, 69, 6649, "Ansh", "Daddys")
print(a)

no = a.count(69)
print(no)

i = a.index("Ansh")
print(i)


print(len(a))




                                # Some more tuples methods
                                
                                
                
# Creating tuples
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7)

# Indexing and slicing
print("Indexing and Slicing:")
print("t1[2]:", t1[2])          # Output: 3
print("t1[1:3]:", t1[1:3])      # Output: (2, 3)

# Concatenation and repetition
concatenated = t1 + t2
repeated = t1 * 2
print("\nConcatenation and Repetition:")
print("t1 + t2:", concatenated)  # Output: (1, 2, 3, 4, 5, 6, 7)
print("t1 * 2:", repeated)       # Output: (1, 2, 3, 4, 1, 2, 3, 4)

# Tuple methods
count_2 = t1.count(2)
index_3 = t1.index(3)
print("\nTuple Methods:")
print("t1.count(2):", count_2)  # Output: 1
print("t1.index(3):", index_3)  # Output: 2

# Built-in functions
length_t1 = len(t1)
max_t1 = max(t1)
min_t1 = min(t1)
sum_t1 = sum(t1)
print("\nBuilt-in Functions:")
print("len(t1):", length_t1)  # Output: 4
print("max(t1):", max_t1)    # Output: 4
print("min(t1):", min_t1)    # Output: 1
print("sum(t1):", sum_t1)    # Output: 10

# Packing and Unpacking
packed = (1, 2, 3)
a, b, c = packed
print("\nPacking and Unpacking:")
print("Packed:", packed)       # Output: (1, 2, 3)
print("Unpacked values:", a, b, c)  # Output: 1 2 3

# Nested tuples
nested = (1, (2, 3), 4)
nested_value = nested[1][0]
print("\nNested Tuples:")
print("nested[1][0]:", nested_value)  # Output: 2

# Creating single-element tuple
single_element = (1,)
print("\nSingle-element Tuple:")
print("single_element:", single_element)  # Output: (1,)

# Converting between tuples and lists
