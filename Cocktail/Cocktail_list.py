import random
import json


class CocktailList:
    """ Класс для работы с json"""
    def __init__(self, file: str = './result.json'):
        with open(file, encoding='utf - 8') as file:
            self.data = json.load(file)

        self.get_list_tags = self.__get_list_tags()
        self.__lst_tags__ = [i for i in range(len(self.data))]

    def __get_list_tags(self):
        """ Сбор всех тегов коктейлей """
        lst_tags = []
        for y in self.data:
            for x in y['Tags'].split(' / '):
                if x in lst_tags:
                    continue
                else:
                    lst_tags.append(x)

        return lst_tags

    def get_random_cocktail_list(self):
        """ Функция для перемешивания коктейлей """
        random.shuffle(self.__lst_tags__)
        return iter(self.__lst_tags__)
