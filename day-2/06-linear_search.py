list_of_envs=['dev', 'test', 'prod']

i='testing'
found=False

for env in list_of_envs:
    if i == env:
        found=True
        
if found:
    print("env found")
else:
    print("env not found")