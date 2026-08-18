#Given the following code, identify whether the variable 'count' is local or global in each function, and explain what will be printed when run:

count = 10
def update_count():
    count = 5
    print('Inside:', count)

update_count()
print('Outside:', count)


'''Outputs
count = 10 is a global variable, because it's creat outside the function.
Inside the update_count() function, count = 5 is a local variable, because it's creat inside the function.
We call update_count(), the function uses it's local count, so it print Inside: 5.

After the function finishes, the local variable is gone. The global count is still 10, so it prints Outside: 10.

'''



