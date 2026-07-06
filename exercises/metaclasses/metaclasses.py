class PluginMeta(type):
    """
    Metaclass for plugins
    """
    plugin_registry = {}
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name != 'Plugin':
            PluginMeta.plugin_registry[name] = cls

class Plugin(metaclass=PluginMeta):
    """
    Base class for plugins
    """
    pass
class AudioPlugin(Plugin):
    """
    Audio plugin
    """
    pass

class VideoPlugin(Plugin):
    """
    Video plugin
    """
    pass

print(PluginMeta.plugin_registry)  # Output: {'AudioPlugin': <class '__main__.AudioPlugin'>, 'VideoPlugin': <class '__main__.VideoPlugin'>}