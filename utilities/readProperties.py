import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName(username_number):
        key = f'username{username_number}'
        return config.get('common info', key)

    '''@staticmethod
    def getUserName1():
        username = config.get('common info', 'username1')
        return username

    @staticmethod
    def getUserName2():
        username = config.get('common info', 'username2')
        return username

    @staticmethod
    def getUserName3():
        username = config.get('common info', 'username3')
        return username

    @staticmethod
    def getUserName4():
        username = config.get('common info', 'username4')
        return username'''

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
