import json
import yaml


def main():
    with open('sample.json', 'r') as file1:
        with open('sample.yaml', 'w') as file2:
            json_data = json.loads(file1.read())
            converted_json_data = json.dumps(json_data)

            yaml_data = yaml.safe_load(converted_json_data)
            converted_yaml_data = yaml.dump(yaml_data)

            file2.write(converted_yaml_data)


if __name__ == '__main__':
    main()
