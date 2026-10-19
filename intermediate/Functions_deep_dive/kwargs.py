# **kwargs
# This collects extra named arguments into a dict. It’s handy for filters and options.

def show_config(**options):
    for key, value in options.items():
        print(key, "=", value)

show_config(threshold=3, window=10, verbose=True)