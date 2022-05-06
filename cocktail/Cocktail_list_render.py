class CocktailRenderList:
    @staticmethod
    def show_tags(tags):
        result = [tags[i:i + 4] for i in range(0, len(tags), 4)]
        result = [' / '.join(item) for item in result]
        result = '\n'.join(result)
        return result






