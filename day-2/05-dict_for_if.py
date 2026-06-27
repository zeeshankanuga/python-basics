server1={
    "env": "development",
    "cloud": "aws",
    "region": "us-east-1",
    "instance_type": "t2.micro",
    "active": True
}

server2={
    "env": "production",
    "cloud": "aws",
    "region": "us-west-1",
    "instance_type": "t2.medium",
    "active": False
}

server=[server1, server2]

for env in server:
    for key, value in env.items():
        if key == "active" and value == True:
            print("server deployed")
            print("env: ", env["env"])
            print(env.keys())