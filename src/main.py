from public.API import Cityflow_API
from dotenv import load_dotenv
import os



load_dotenv()
config = os.getenv("CONFIG_JSON_FILE")
api = Cityflow_API(config)
api.start()