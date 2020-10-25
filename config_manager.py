import yaml
class ConfigManager:
    def __init__(self):
        with open('config.yml') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
    def get(self,key):
        try: 
            return self.config[key]
        except(KeyError):
            pass