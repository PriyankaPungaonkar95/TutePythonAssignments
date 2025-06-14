# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(text_to_write + '\n')
print("Data successfully written to output.txt.")

# Step 2: Append additional input to the same file
text_to_append = input("\nEnter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(text_to_append + '\n')
print("Data successfully appended.")

# Step 3: Read and display final content of the file
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    print(file.read())