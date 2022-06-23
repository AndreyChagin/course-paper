class CocktailRenderList:
    """ Класс для работы с тегами """
    @staticmethod
    def show_tags(tags):
        """ Функция для обработки вывода тегов """
        result = [tags[i:i + 4] for i in range(0, len(tags), 4)]
        result = [' / '.join(item) for item in result]
        result = '\n'.join(result)
        return result
