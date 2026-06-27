list_of_cloud_names = list(['AWS', 'Azure', 'GCP'])

list_of_envs = ['dev', 'test', 'prod']
list_of_envs.append('uat')

print(type(list_of_cloud_names))
print(type(list_of_envs))

print(dir(list_of_envs))

print(list_of_envs.append.__doc__)


print(list_of_envs.insert(1, 'staging'))

for i in list_of_envs:
    print("deploying to environment: ", i)
    print(i)