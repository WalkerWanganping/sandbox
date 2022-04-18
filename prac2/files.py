#Q1
name = input("please enter your name：")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()


#Q2
in_file = open("name.txt","r")
output_name = in_file.read()
print(f"your name is", output_name)
in_file.close()


#Q3
numbers_text = """17
42
400"""
out_file = open("numbers.txt","w")
out_file.write(numbers_text)
out_file.close()
in_file = open("numbers.txt","r")
num_1 = int(in_file.readline())
num_2 = int(in_file.readline())
total_number = num_1 + num_2
print(total_number)
in_file.close()


#Q4
in_file = open("numbers.txt","r")
for line in in_file:
    print(line.strip())
in_file.close()