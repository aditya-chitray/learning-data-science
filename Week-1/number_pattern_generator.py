def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    
    elif n<1:
        return 'Argument must be an integer greater than 0.'
    
    else:
        pattern = ''
        for i in range(1,n+1):
            pattern += str(i) + ' '
        return pattern.rstrip()

print(number_pattern(12))