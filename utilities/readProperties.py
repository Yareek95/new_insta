import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName1():
        username = config.get('common info', 'username1')
        return username

    @staticmethod
    def getUserName2():
        username = config.get('common info', 'username2')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getSearchName():
        search_name = config.get('common info', 'search_name')
        return search_name