# Sample array
my_array = [1, 2, 3, 4, 5]

# Iterate over pairs of adjacent elements
for current_item, next_item in zip(my_array, my_array[1:] + [None]):
    print(f"Current Item: {current_item}, Next Item: {next_item if next_item is not None else 'No Next Item'}")
print(f"\n\nmy-array: {my_array[1:] + [None]}")