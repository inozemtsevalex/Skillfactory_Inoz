import os

print(os.getcwd())
with open('/Users/aleksandrinozemcev/projects/Skillfactory/input.txt', 'r') as input_file:
    with open('/Users/aleksandrinozemcev/projects/Skillfactory/output.txt', 'w') as output_file:
        for i in input_file:
            output_file.write(i)


