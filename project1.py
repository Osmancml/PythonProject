# liste örnek olarak kullanılması için patika tarafından verilmiştir.
# iç içe geçmiş listeleri tek listede toplar

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if type(item) == list:
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)
    
    return flat_list

print(flatten_list(input_list))
