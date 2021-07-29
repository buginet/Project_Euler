### one line code using sets
sum(x for x in range(1000) if x%3==0 or x%5==0)



### if n is changeable, apply code below.

def sum_two_common_multiples(n1, n2, under_number):
    n1_list = [x for x in range(under_number) if x%n1==0]
    n2_list = [x for x in range(under_number) if x%n2==0]
    
    result = sum(list(set(n1_list)|set(n2_list)))
    print(result)
    return result
    
sum_two_common_multiples(3,5,1000)
