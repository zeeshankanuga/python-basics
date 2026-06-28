# list_of_envs=['dev', 'test', 'prod']

# i='testing'

def linear_search(list_of_envs, i):
    found=False
    for env in list_of_envs:
        if i == env:
            found=True

    return found
        
# found = linear_search(list_of_envs,i)
# print(found)