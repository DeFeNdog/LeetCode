
def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))

# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))



# def versionCompare(version1, version2):
#     v1 = version1.split(".")
#     v2 = version2.split(".")
#     n, m = len(v1), len(v2)

#     v1 = [int(i) for i in v1]
#     v2 = [int(i) for i in v2]

#     if n < m:
#         for i in range(n, m):
#             v1.append(0)

#     if m < n:
#         for i in range(m, n):
#             v2.append(0)

#     for i in range(len(v1)):
#         if v1[i] > v2[i]:
#             return 1
#         elif v2[i] > v1[i]:
#             return -1


# ans = versionCompare("1.1", "1.10")
# print(ans)
