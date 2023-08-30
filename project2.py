# liste örnek olarak kullanılması için patika tarafından verilmiştir.
# iç içe listeleri ve genel listeyi ters çevirir.

input=[[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(k):
 k = k[::-1]
 k = [i[::-1] for i in k]
 return k

print(reverse_list(input))