import configparser


class ConfigFileHelper:
    def __init__(self) -> None:
        self._parser = configparser.ConfigParser()

    def get_config(self, env: str):
        self._parser.read(f"./config/{env}.conf")
        return {i[0]: i[1] for i in self._parser['PROJECT'].items()}
