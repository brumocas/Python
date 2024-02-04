def print_pattern(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes = "#" * i
        print(spaces + hashes + "  " + hashes)


height = 0

while height > 8 or height < 1:
    try:
        height = int(input("Enter the height: "))
    except:
        continue
print_pattern(height)
