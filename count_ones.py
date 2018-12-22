__author__ = "vinayak"


def executor_ones(bin_num):
    valid = check_for_validity(bin_num)
    if valid:
        output = check_longest_ones (bin_num)
        for i in range(len(bin_num)):
            if bin_num[i] == '0':
                greater_len = swap_and_check(bin_num, i, output)
                if greater_len > output:
                    output = greater_len
        print("The greatest length of number of ones in the given input {} is {}".format(bin_num,output))

def check_for_validity(bin_num):
    bin = ['0', '1']
    for i in bin_num:
        if i in bin:
            pass
        else:
            print(" Invalid binary number, please enter 0's and 1's")
            return False
    return True

def swap_and_check(bin_num, index, output):
    for j in range(len(bin_num)):
        bin_num_list = list(bin_num)
        bin_num_list[j], bin_num_list[index] = bin_num_list[index], bin_num_list[j]
        checked_val = check_longest_ones(bin_num_list)
        if checked_val > output:
            output = checked_val
    return output


def check_longest_ones(bin_num):
    cnt_ones = 0
    ones =0
    if '0' not in bin_num:
       ones = len(bin_num)
    else:
        for k in range(len(bin_num)):
            if bin_num[k] == '1':
                cnt_ones = cnt_ones + 1
                if cnt_ones > ones:
                    ones = cnt_ones
            else:
                cnt_ones = 0
    return ones


if __name__ == "__main__":
    binary_input = input(" Enter the binary number: ")
    executor_ones(binary_input)


