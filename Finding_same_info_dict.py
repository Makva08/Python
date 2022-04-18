ppl = {'1': {'name': ['irakli'], 'languages':['Python,C++.Java'] },
'2': {'name': ['leo'], 'languages': ['english, math, science'] },
'3': {'name': ['irakli'], 'languages': ['Python,C++.Java'] },
'4': {'name': ['gio'], 'languages': ['english, math, science'] }, }

for i in ppl:
    for x in ppl:
        if ppl[str(i)]['name'] == ppl[str(x)]['name'] and i != x and ppl[str(i)]['languages'] == ppl[str(x)]['languages']:
            print(ppl[str(i)])
            print("Here is the imposter")
        break
