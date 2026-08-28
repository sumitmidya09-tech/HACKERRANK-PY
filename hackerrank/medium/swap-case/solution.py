def swap_case(s):
    z=list(s)
    for i in range(len(z)):
        if z[i]==z[i].lower():
            z[i]=z[i].upper()
        else:
            z[i]=z[i].lower()
    return "".join(z)

