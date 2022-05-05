import json
import random
with open('result.json', encoding='utf-8') as file:
    data = json.load(file)


lst_tags = list()

for y in data:
    for x in y['Tags'].strip().split(' /  '):
        if x in lst_tags:
            continue
        else:
            lst_tags.append(x)


lst_tags = [lst_tags[i:i + 4] for i in range(0, len(lst_tags), 4)]
lst_tags = [' / '.join(item) for item in lst_tags]
lst_tags = '\n'.join(lst_tags)

lst = [i for i in range(950)]
random.shuffle(lst)

