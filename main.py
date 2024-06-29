import sys
import os

# Додати шлях до src у sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from config_parser import load_config
from config_validator import validate_config

config = load_config("tests/test_config.json")
schema = load_config("tests/test_schema.json")

is_valid = validate_config(config, schema)
if is_valid:
    print("Config is valid")
else:
    print("Config is invalid")
