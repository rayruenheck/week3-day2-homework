places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print([place for place in filter(lambda empty_string: empty_string != ''and empty_string != ' ' and empty_string != '  ', places)])


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def namesort(author):
    author.sort(key=lambda name: name.split()[-1])
    return author
print(namesort(author))



# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


print([degree for degree in map(lambda degree: (degree[0], degree[1]*(9/5)*32), places)])













def fib(n):
    if n <= 1:
        return 1
    
    return(fib(n-1) + fib(n-2))

def print_fib(n):
    
    for i in range(n + 1):
        print('iteration', str(i)+':',fib(i))
    
        
print_fib(5)
