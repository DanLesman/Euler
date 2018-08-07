sum = 0
for i in range(1,1000):
	var = 1000 - i
	if var%3 is 0 or var%5 is 0:
		sum+=var
print (sum)
mystring = "hello"
for c in mystring:
	print("letter:" + c)