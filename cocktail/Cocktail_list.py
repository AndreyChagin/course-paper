import json
import random


class CocktailList:
    def __init__(self, file: str = './result.json'):
        with open(file, encoding='utf - 8') as file:
            self.data = json.load(file)

        self.get_list_tags = self.__get_list_tags()
        self.__lst_tags__ = [i for i in range(len(self.data))]
        self.__iter = iter(self.__lst_tags__)

    def __get_list_tags(self):
        lst_tags = []
        for y in self.data:
            for x in y['Tags'].split(' / '):
                if x in lst_tags:
                    continue
                else:
                    lst_tags.append(x)

        return lst_tags

    def get_random_cocktail_list(self):
        random.shuffle(self.__lst_tags__)
        return iter(self.__lst_tags__)

    def get_random_cocktail(self):
        return self.data[next(self.__iter)]

    def reset_random(self):
        random.shuffle(self.__lst_tags__)
        self.__iter = iter(self.__lst_tags__)


