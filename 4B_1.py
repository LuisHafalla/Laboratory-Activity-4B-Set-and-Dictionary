# Define sets A, B, and C
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# (a) Count and display elements in A or B (union)
union_AB = A | B
print("\n(a) Elements in either A or B:", sorted(union_AB))
print("Total count:", len(union_AB))

# (b) Identify elements in B that are not in A or C
unique_B = B - (A | C)
print("\n(b) Elements in B but not in A or C:", sorted(unique_B))
print("Total count:", len(unique_B))

# (c) Various set operations

# (i) Elements in C but not in A or B
print("\n(c.i) Elements in C excluding A and B:", sorted(C - (A | B)))

# (ii) Elements that are common in all three sets
common_ABC = A & B & C
print("\n(c.ii) Common elements in A, B, and C:", sorted(common_ABC))

# (iii) Elements that belong to either (A ∩ B) or (B ∩ C)
intersect_AB_BC = (A & B) | (B & C)
print("\n(c.iii) Elements in (A ∩ B) or (B ∩ C):", sorted(intersect_AB_BC))

# (iv) Elements found in both A and C but not in B
AC_excluding_B = (A & C) - B
print("\n(c.iv) Elements in (A ∩ C) but not in B:", sorted(AC_excluding_B))

# (v) Elements that appear in all three sets (A, B, and C)
print("\n(c.v) Elements present in A, B, and C:", sorted(common_ABC))

# (vi) Elements exclusive to B (not in A or C)
unique_to_B = B - (A | C)
print("\n(c.vi) Elements unique to B:", sorted(unique_to_B))
