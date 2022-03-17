import configparser


class SettingsException(Exception):
    def __init__(self, message):
        """
        Creates an object of type SettingsException
        :param message: The message of the SettingsException, a string
        """
        super().__init__(message)


class Settings:
    def __init__(self, file_name):
        """
        Creates an object of type Settings
        :param file_name: The location of the file containing the settings
        """
        self.__file_name = file_name
        self.__load()

    def __load(self):
        """
        Reads the settings file and loads the settings into the program
        :return: nothing
        """
        config = configparser.ConfigParser()
        config.read(self.__file_name)
        self.__dimension = int(config.get("DEFAULT", "DIM").strip("\""))
        self.__apple_count = int(config.get("DEFAULT", "apple_count").strip("\""))

    @property
    def dimension(self):
        return self.__dimension

    @property
    def apple_count(self):
        return self.__apple_count
