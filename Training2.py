def in_array(array1, array2):
    return ([word for word in array1 if any(word in sub for sub in array2)])
print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))