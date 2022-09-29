import zipfile


stat = {}
hash_path = {}

with zipfile.ZipFile('/Users/nuraim/Downloads/names.txt.zip') as zipf:
    with zipf.open("names.txt", "r") as f:
        for _ in range(100_000_000):
            hash_string = next(f).decode('utf-8')

            hash_head, hash_tail = hash_string[:3], hash_string[3:]
            stat[hash_head] = stat.setdefault(hash_head, 0) + 1

            cursor = hash_path
            last_key = None
            for k in hash_head:
                last_key = k
                cursor = cursor.setdefault(k, {})

            cursor[last_key] = hash_tail


sorted_keys = sorted(stat, key=stat.get, reverse=True)


print(len(stat))
for i in sorted_keys[:10]:
    print(stat[i])