import yaml

with open("./config.json", "r") as json_file:
    data = yaml.safe_load(json_file)

data["status"] = "Maintenance"

with open("./config.yaml", "w") as yaml_file:
    yaml.dump(data, yaml_file)

