st1 = "   NGuyen van   hOAng   "

st2 = st1.lower()

st3 = st2.strip().split()

st4 = []
for item in st3:
    st4.append(item)

st5 = " ".join(st4)

st6 = st5.title()

print(st6)