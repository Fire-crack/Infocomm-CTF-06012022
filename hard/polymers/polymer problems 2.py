# This question is a continuation of "polymer problems 1", in the medium section.
# Completion of that question is encouraged but not neccessary
# 
# 
# in your input file, you should see two different sets of inputs,
# For example:

# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# 
# The first line is the polymer template - this is the starting point of the process.

# The following section defines the pair insertion rules. 
# A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. 
# These insertions all happen simultaneously.

# So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

#   The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
#   The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
#   The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
# Note that these pairs overlap: the second element of one pair is the first element of the next pair. 
# Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

# After the first step of this process, the polymer becomes NCNBCHB.

# Here are the results of a few steps using the above rules:

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# This polymer grows quickly. After step 5, it has length 97. After step 10, it has length 3073. 
# 
# After step 500, 
# B occurs 6546781215792283740026379393496215428733515461101084891868528717981849284084377359175250116153308869837215513900610098785753398323481251733862542294860 times, 
# C occurs 149487940974704788111211130692649783562363849572889654021392999248014326918544473088230162277599313425735053303076666666073 times, 
# H occurs 87822662295626675487433381988387965089692366734836404329328946987804808793269534838161854922426996015910449519152983334187 times, 
# N occurs 3273390607896141870013189696749271424646079213429464963900307637654495888821920247123838214588584465903630530555678097041872061872529424603893390473009 times
# By taking the quantity of the most common element (B, 6546781215792283740026379393496215428733515461101084891868528717981849284084377359175250116153308869837215513900610098785753398323481251733862542294860) 
# and subtracting the quantity of the least common element (H, 87822662295626675487433381988387965089692366734836404329328946987804808793269534838161854922426996015910449519152983334187),
# It produces 6546781215792283740026379393408392766437888785613651509880140752892156917349540954845921169165504061043945979062448243863326402307570802214709558960673.

# Apply 500 steps of pair insertion to the polymer template and find the most and least common elements in the result. 
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
# 
# (The flag will be CTFInfocomm{quantity})
