import jsonschema
import json
import yaml

def validate_config(config, schema):
    try:
        jsonschema.validate(instance=config, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        print(f"Validation error: {err}")
        return False

def load_config(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate a configuration file against a schema.")
    parser.add_argument("config_path", help="Path to the configuration file")
    parser.add_argument("schema_path", help="Path to the schema file")
    args = parser.parse_args()
    
    config = load_config(args.config_path)
    schema = load_config(args.schema_path)
    
    is_valid = validate_config(config, schema)
    if is_valid:
        print("Config is valid")
    else:
        print("Config is invalid")

if __name__ == "__main__":
    main()
