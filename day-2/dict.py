dict_of_items1 = {
    "env": "development",
    "cloud": "aws",
    "region": "us-east-1",
    "instance_type": "t2.micro",
    "active": True
}

dict_of_items2 = {
    "env": "production",
    "cloud": "aws",
    "region": "us-east-1",
    "instance_type": "t2.medium",
    "active": True
}

print(dict_of_items1.get("env"))
print(dict_of_items2.get("env"))

env_list = [dict_of_items1, dict_of_items2]

if dict_of_items1["active"]:
    print("server deployed")
    print("env: ", dict_of_items1["env"])

if dict_of_items2["active"]:
    print("server deployed")
    print("env: ", dict_of_items2["env"])

for env in env_list:
    for key, value in env.items():
        print(key, ":", value)