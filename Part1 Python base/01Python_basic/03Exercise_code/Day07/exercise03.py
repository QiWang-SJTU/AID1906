# for r in range(4):
#     for c in range(5):
#         if r % 2:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

for i in range(4):
    for j in range(i + 1):
        print("*", end=" ")
    print()
