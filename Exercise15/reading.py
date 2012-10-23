def mystery1(inp):
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base
    
def mystery2(inp):
    if not inp:
        return 0
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    return num

def mystery3(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    

def mystery4(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    return inp
    
def mystery5():
    inp = open("sample_input.txt")
    ws = inp.split()
    h = dict()
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)

def mystery6(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = tmp
                swapped = True

def mystery7(inp):
    a, b = 0, 1
    for i in range(inp):
        a, b = b, a + b
    return a

def mystery8(inp):
    if inp <= 0:
        return 0
    if inp == 1:
        return 1
    return mystery8(inp - 1) + mystery8(inp - 2)

def mystery9(inp1, inp2):
    if len(inp1) == len(inp2):
        for i in range(len(inp1)):
            if inp1[i] != inp2[i]:
                return False
        return True
    return False

def mystery10(inp1, inp2):
    outp = {}
    for k, v in inp1.items():
        if k in inp2:
            outp[k] = v + inp2[k]
    return outp

def mystery11(inp):
    outp = {}
    for s in inp:
        if s:
            outp.setdefault(s[0], []).append(s)
    return outp

def mystery12(inp):
    best_i, best_j = 0, 0
    for i in range(len(inp)):
        for j in range(len(inp), i, -1):
            if inp[i:j] == inp[i:j][::-1]:
                if j - i > best_j - best_i:
                    best_i = i
                    best_j = j
    return inp[best_i:best_j]

def mystery13(inp_a, inp_e):
    while len(inp_a) > 1:
        if inp_e == inp_a[len(inp_a) / 2]:
            return True
        elif inp_e < inp_a[len(inp_a) / 2]:
            inp_a = inp_a[:len(inp_a) / 2]
        else:
            inp_a = inp_a[len(inp_a) / 2 + 1:]

    return len(inp_a) > 0 and inp_e == inp_a[0]

def mystery_m(inp1, inp2):
    i, j = 0, 0
    outp = []
    while i < len(inp1) and j < len(inp2):
        if inp1[i] <= inp2[j]:
            outp.append(inp1[i])
            i += 1
        if inp1[i] >= inp2[j]:
            outp.append(inp2[j])
            j += 1
    if i < len(inp1):
        outp.extend(inp1[i:])
    elif j < len(inp2):
        outp.extend(inp2[j:])

    return outp

def mystery_s(inp):
    if len(inp) < 2:
        return inp

    fh = mystery_s(inp[:len(inp) / 2])
    sh = mystery_s(inp[len(inp) / 2:])

    return mystery_m(fh, sh)
