def testfun():
    print("welcometo falconx")
    yield
    print("teardown conn")

print('test...')
i=0
iter = testfun()
# while next(iter) in [None]:  surfaces exception
# 
while next(iter):
    # print(t)
    # print(f"val {val}")
    i+=1
    print(i)
    if i == 5:
        break

for i in testfun():
    print(f"i = {i}")
#     # testfun()
# testfun()
# testfun()