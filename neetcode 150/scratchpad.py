# nums = [1,2,2,3,3,3]
# k = 2
# nums = [7,7]
# k = 1
nums=[4,1,-1,2,-1,2,3]
k=2
hashmap = {}
for i in range(len(nums)):
    hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

print(f"{hashmap} hashmap")

blank = []
for x in range(len(nums)):
    blank.append(hashmap[nums[x]])
print(blank)
# print(f"{sorted(set(blank), reverse=True)} list")
new_list = sorted(set(blank), reverse=False)
top_freq = new_list[-k:]
answer = []
for keys in hashmap:
    if hashmap[keys] in top_freq:
        answer.append(keys)