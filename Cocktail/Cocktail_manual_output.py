class OutputManual:
    def __init__(self, x: dict):
        self.__output_manual_dict = x
        self.output_manual = self.__output()

    def __output(self):
        return "\n".join([str(key) + ". " + str(value) for key, value in self.__output_manual_dict.items()])
