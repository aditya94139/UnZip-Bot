import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("6993461096:AAHWzXylmaIbTJndWDTvQKBta00mmXUVOWI", "")
    API_ID = int(os.environ.get("25586552", ))
    API_HASH = os.environ.get("f265cba9d76dc6ad70914accbe758f47", "")
    
    
