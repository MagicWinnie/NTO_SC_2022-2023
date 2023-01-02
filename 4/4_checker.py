import combinatorics_4
import permutation_4

print("k0\tk1\tcomb\tperm")
for k0 in range(3, 6):
    for k1 in range(k0, 10):
        res_comb = combinatorics_4.runner(k0, k1)
        res_perm = permutation_4.runner(k0, k1)
        if res_comb != res_perm:
            print(k0, k1, res_comb, res_perm, sep='\t')
