# dictionary =A changeable , unordered collection of unique key:value pairs fast because they use hashing
#  allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'berlin'})
capitals.pop('China')
capitals.clear()

#print(capitals['Russia'])

#print(capitals.get('Germany'))
#print(capitals.key())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)