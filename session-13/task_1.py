#Write a recursive function in Python called reverse_string(s)
# that takes a string and returns it reversed (e.g., 'hello' becomes 'olleh').



def reverse_string(n):
    if len(n) == 0:
        return n
    return reverse_string(n[1:]) + n[0]

new_reverse = reverse_string("Helloo")
print(new_reverse)

