import time

# for i in range(10):
#     print(i)

# for i in range(5,11):
#     print(i)
    
# for i in range (0,21,2):
#     print(i)

i = 0
while i < 5:
    print(i)
    i = i + 1 #(i += 1) is also valid
    
while True:
    time.sleep(2)
    print("Hello World")