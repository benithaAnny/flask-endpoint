
users = [{'id': 1}, {'id': 2}, {'id': 3},{'id': 2}]

unique_users = []
for i in range(len(users)):
    seen = False
    for j in range(len(unique_users)):
        if users[i] == unique_users[j]:
            seen = True
            break
    if not seen:
        unique_users.append(users[i])
