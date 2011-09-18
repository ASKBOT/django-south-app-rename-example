import os
def get_app_name():
    """returns name of the current app"""
    return os.path.basename(os.path.dirname(__file__))

