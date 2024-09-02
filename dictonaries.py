
physic = {'jamac':70,'abdi':69,'hussein':2}
math = {'abdala':60,'jaac':88,'hassan':1}


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with the first dictionary's items
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum values if key is in both dictionaries
        else:
            merged_dict[key] = value  # Add new key-value pair
    return merged_dict
print(merge_dicts(physic, math))