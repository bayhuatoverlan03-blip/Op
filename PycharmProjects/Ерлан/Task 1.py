import datetime

class ConfigStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)


# DEMO
if __name__ == "__main__":
    config1 = ConfigStorage()
    config2 = ConfigStorage()

    config1.set("username", "admin")
    config2.set("start_time", str(datetime.datetime.now()))

    print(config1.data)
    print(config2.data)
    print("Один объект? ->", config1 is config2)
