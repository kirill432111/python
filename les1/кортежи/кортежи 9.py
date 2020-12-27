Ralph="""The new life to which he had been called opened pleasantly and increased in happiness and opportunity,
except for the sadness of bereavements, for, in the first few years,
his brilliant brothers Edward and Charles died, and soon afterward Waldo, his firstborn son,
and later his mother. Emerson had left traditional religion,
the city, the Old World, behind, and now went to Nature as his teacher, his inspiration."""
Ralph=Ralph.split()
slovar={}
for i in Ralph:
    for j in Ralph:
        if i == j:
            count=count+1
            slovar[i]=(count)
    count=0
print(slovar)
print()