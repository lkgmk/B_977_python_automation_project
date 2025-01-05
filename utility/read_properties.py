import configparser

config = configparser.RawConfigParser()
# config.read(r".\\configuration\\config.ini")
config.read(r"C:\Users\Dhanashri Thorat\Desktop\gitcheck\B_977_python_automation_project\configuration\config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get("common info", "base_url")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password
