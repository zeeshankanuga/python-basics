cloud_env=['aws','gcp','azure']

try:
    print(cloud_env[20])
except:
    print("Cloud environment not found")
finally:
    print("Finally block")
    
print("End of program")