



# files = ('12.docx')

# f = open('file', 'r', encoding='utf-8')
# f.close()


# for path in files:
#     with open(path, 'r', encoding='ascil') as f:
#         print(path)
#         print(f.read())





# print(f)
# print(f.read())







# total = 0
# for line in stdin:
#     for number in line.split():
#         total += int(number)
#     # if total > 100:
#     #     break
# print(total)

# s = 'id|name\n1|Женя\n2|Арсен'
# s = ['id|name', '1|Женя', '2|Арсен']
# # s = [(1, 'Женя'), (2, 'Арсен')]

# with open('file.csv', 'w', encoding='utf-8') as f:
#     # f.write(
#     #     '\n'.join([f'{id}|{name}' for id, name in s])
#     # )
#     f.writelines(s)

# with open('numbers.txt') as file:
#     total = 0
#     for line in file:
#         for number in line.split():
#             total += int(number)

#     print(total)


users = []
with open('users.txt', encoding='utf-8') as file:
    print(file.readlines())
    # for line in file:
    #     users.append(line.strip('\n'))


# with open('sorted_users.txt', 'w', encoding='utf-8') as file:
#     file.writelines([user + '\n' for user in sorted(users)])



# words = []
# with open('lines.txt') as file:
#     for line in file:
#         for s in line.strip('\n').split():
#             if s.isalpha():
#                 words.append(s)
# print(max(words, key=len))
