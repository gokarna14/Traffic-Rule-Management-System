def number_iteration_divisible_by(num_to_divide, higher_range, lower_range=0):
    return_list = []
    for i in range(lower_range, higher_range+1):
        if i % num_to_divide == 0:
            return_list.append(str(i))
            yield i


def numbers_sum_boolean(sum_, n1=0, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, n8=0, n9=0, n10=0):
    if sum_ == n1+n2+n3+n4+n5+n6+n7+n8+n9+n10:
        return True
    else:
        return False


def not_equal_to(q=0, w=0, e=0, r=0):
    a = [q, w, e, r]
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
    return True
