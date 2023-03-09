



names = ('Саша', 'Маша', 'Паша')

# print(
#     '\n'.join(
#         [
#             f'{i}) {name}'
#             for i, name in enumerate(
#                 [
#                     name
#                     for name in names if len(name) == 4
#                 ],
#                 1
#             )
#         ]
#     )
# )
# print('\n'.join([f'{i}) {name}' for i, name in enumerate([name for name in names if len(name) == 4], 1)]))

lst = zip(range(1, 4), names)
print(lst)
for i, name in zip(range(1, 4), names):
    print(f'{i}) {name}')
