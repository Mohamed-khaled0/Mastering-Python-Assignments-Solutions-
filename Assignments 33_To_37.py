# 1

print(bool(True))
print(bool(100.95))
print(bool(2))
print(bool(['dd','dd']))
print(bool({'ss'}))


print(bool(False))
print(bool())
print(bool(0))
print(bool([]))
print(bool({}))

print("-" * 100)

# 2
html = 80
css = 60
javascript = 70

# Needed Output
#True
print(html >50 and css > 50 and javascript >50)

print("-" * 100)

# 3

num_one = 10
num_two = 20
num = 20

# Needed Output
#True
#False

print(num > num_one or num > num_two )
print(num > num_one and num > num_two )


print("-" * 100)

# 4
num_one = 10
num_two = 20

# Needed Output

#30
#27000
#1000
#200.0
#<class 'str'>

result = num_one + num_two
print(result)
result**=3
print(result)

result%=26000
print(result)
result/=5
print(result)
print(type(str(result)))
