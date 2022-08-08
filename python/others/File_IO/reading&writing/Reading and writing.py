def sum_number_pairs(input_file, output_filename):
    output_file = open(output_filename, 'w')
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)
    output_file.close()

sum_number_pairs(open('number_pairs.txt', 'r'), 'out.txt')