# l = [0, 1, 2]
# combinations = []

# for i in l:
#     for m in l:
#         k = [m]
#         for j in l:
#             if j not in k:
#                 k.append(j)
#         combinations.append("".join(map(str, k)))

# print(combinations)

# def generate_permutations(arr, start, end, result):
#     if start == end:
#         result.append("".join(map(str, arr)))
#     else:
#         for i in range(start, end + 1):
#             arr[start], arr[i] = arr[i], arr[start]
#             generate_permutations(arr, start + 1, end, result)
#             arr[start], arr[i] = arr[i], arr[start]

input_str="CAT"
result = [input_str]

for i in range(len(input_str)):
    size = len(result)

    for j in range(size):
        current = list(result[j])

        for k in range(i + 1, len(input_str)):
            current[i], current[k] = current[k], current[i]
            result.append(''.join(current))
          # swapping the two values
            current[i], current[k] = current[k], current[i]
# know printing the result value one bv one
for permutation in result:
  print(permutation)

# generate_permutations(l, 0, len(l) - 1, combinations)
# print(combinations)
