st = "Python Programming is fun"
sub = "n"

pos = st.find(sub)
while pos >= 0:
    print("Found at ", pos)
    pos = st.find(sub, pos + 1)
