import pytest
from src.config_validator import validate_config, load_config

def test_validate_valid_config():
    config = load_config('tests/test_config.json')
    schema = load_config('tests/test_schema.json')
    assert validate_config(config, schema) == True

def test_validate_invalid_config():
    config = load_config('tests/invalid_config.json')
    schema = load_config('tests/test_schema.json')
    assert validate_config(config, schema) == False
