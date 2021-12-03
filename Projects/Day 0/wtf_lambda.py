# Lambda is a anomynus function, means we can make function for quick use

add_one = lambda a : a + 1 
print(add_one(15))

add_two = lambda b : add_one(b) + 1
print(add_two(15))

# Simple