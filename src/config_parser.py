import json
import yaml

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
    parser = argparse.ArgumentParser(description="Load a configuration file.")
    parser.add_argument("file_path", help="Path to the configuration file")
    args = parser.parse_args()
    
    config = load_config(args.file_path)
    print(config)

if __name__ == "__main__":
    main()
