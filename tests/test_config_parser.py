import pytest
from src.config_parser import load_config

def test_load_json_config():
    config = load_config('tests/test_config.json')
    assert config == {"name": "test", "version": 1}

def test_load_yaml_config():
    config = load_config('tests/test_config.yaml')
    assert config == {"name": "test", "version": 1}

def test_invalid_format():
    with pytest.raises(ValueError):
        load_config('tests/test_config.txt')
