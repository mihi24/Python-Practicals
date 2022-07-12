dict = {'datta': 14,
        'ankit': 55,
        'ankush':33,
        'montu': 55,
        'uday': 70}

print("Sorted by key:")
print(sorted(dict.items(), key=lambda kv: (kv[0], kv[1])))

print("\nSorted by value:")
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))