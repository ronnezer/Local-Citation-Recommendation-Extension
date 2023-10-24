import json

with open('contexts.json', 'r') as file:
    data = json.load(file)

print(data['P15-2138_N04-1019_0'].keys())


# records = []
#
# with open('sample.jsonl', 'r') as file:
#     for line in file:
#         records.append(json.loads(line.strip()))
#
# # for record in records:
# #     print(record['abstract'])
#
# print(records[0])

