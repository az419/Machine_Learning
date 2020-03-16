def sum_to_n(n):
    temp = 0
# for(int a=0; a<n; a++){
    #    temp = temp+a;
    # }

    for i in range(n+1):
        temp = temp + i

    return temp


print(sum_to_n(100))
