import time

user = {}
user["name"] = "사용자"
user["email"] = "user@test.com"
user["age"] = 25


start1 = time.time()
print(user["name"])
end1 = time.time()

print(f"user['name']':::{end1 - start1:.9f} sec")

start2 = time.time()
print(user.get("name"))
end2 = time.time()
print(f"user.get('name'):::{end2 - start2:.9f} sec")

# start1 = time.time()
# status = True if 'status' in user else False
# print(status)
# end1 = time.time()
# print(f"user['name']'::: {end1 - start1:.9f} sec")
#
# start2 = time.time()
# status = user.get('status', False)
# print(status)
# end2 = time.time()
# print(f"user.get('name'):::  {end2 - start2:.9f} sec")