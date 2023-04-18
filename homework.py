places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print([place for place in filter(lambda empty_string: empty_string != ''and empty_string != ' ' and empty_string != '  ', places)])


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def namesort(author):
    author.sort(key=lambda name: name.split()[-1])
    return author
print(namesort(author))



# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


print(list(map(lambda degree: 9/5*degree[-1] +32 if degree[-1] else degree[0], places))) 












def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
    
        
print(fib(6))
