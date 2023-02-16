with open('/Users/aleksandrinozemcev/projects/Skillfactory/numbers.txt', 'r') as input_file:
    min = max = int(input_file.readline())
    for line in input_file:
        num = int(line)
        if min > num:
            min = num
        elif max < num:
            max = num
    sum = max + min
with open('/Users/aleksandrinozemcev/projects/Skillfactory/output.txt', 'w') as output:
    output.write(str(sum))
# filename = '/Users/aleksandrinozemcev/projects/Skillfactory/numbers.txt'
# output = '/Users/aleksandrinozemcev/projects/Skillfactory/output.txt'
#
# with open(filename) as f:
#    min_ = max_ = float(f.readline())  # считали первое число
#    for line in f:
#        num =  float(line)
#        if num > max_:
#            max_ = num
#        elif num < min_:
#            min_ = num
#
#    sum_ = min_ + max_
#
# with open(output, 'w') as f:
#    f.write(str(sum_))
#    f.write('\n')