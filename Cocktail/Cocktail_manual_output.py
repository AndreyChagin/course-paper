class OutputManual:
    """ Класс отвечающий для обработки инструкции """
    def __init__(self, x: dict):
        self.__output_manual_dict = x
        self.output_manual = self.__output()

    def __output(self):
        """ Функция для обработки вывода инструкции """
        return "\n".join([str(key) + ". " + str(value) for key, value in self.__output_manual_dict.items()])
