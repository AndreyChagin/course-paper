import json
import random
with open('result.json', encoding='utf-8') as file:
    data = json.load(file)

set_tags = set()

for y in data:
    for x in y['Tags'].strip().split(' /  '):
        set_tags.add(x)

set_tags = list(set_tags)

set_tags = [set_tags[i:i + 4] for i in range(0, len(set_tags), 4)]
set_tags = [' / '.join(item) for item in set_tags]
set_tags = '\n'.join(set_tags)

lst = [i for i in range(950)]
random.shuffle(lst)

