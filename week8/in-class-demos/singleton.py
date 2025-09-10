class ConfigManager:
    # attribute to store the single instance
    _instance = None

    def __new__(my_singleton_class):
        # Check if an instance already exists
        if my_singleton_class._instance is None: # often cls is used in convention
            # new instance with superclass's __new__ method
            my_singleton_class._instance = super().__new__(my_singleton_class)
            # create a settings collection
            my_singleton_class._instance.settings = {}

        return my_singleton_class._instance


a = ConfigManager()
b = ConfigManager()
a.settings["theme"] = "dark"
print(b.settings["theme"])  # "dark"