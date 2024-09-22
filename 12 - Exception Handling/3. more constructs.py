try:                            # Attempts to execute this code block.
    i = 1
    j = 10 / i
    values = [1, 2]
    sum(values)
except TypeError:               # Runs this block if a TypeError occurs.
    print('TypeError')
    j = 10
except ZeroDivisionError:       # Runs this block if a ZeroDivisionError occurs.
    print('ZeroDivisionError')
    j = 0
else:                           # Executes only if no exceptions were raised.
    print('Else')
finally:                        # Always runs, regardless of exceptions.
    print('Finally')

print(j)
print('End')
