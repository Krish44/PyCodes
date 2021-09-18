exDict = {'MS':['IND',183], 'ABD':['SA',173], 'RP':['AUS',169] ,'CG':['WI',158]}
# Print original dict
print(exDict)

# Print one element
print(exDict['MS'])

# Adding one more value
exDict['SJ'] = ['SL',102]
print(exDict)

# Update Dict member
exDict['SJ'][1] = 139
print(exDict)

# Remove a value
del exDict['CG']
print(exDict)

print(" Country:%s HS:%d" %(exDict['MS'][0], exDict['MS'][1]))