import os

def parse_file(name):
    f = open(name)
    results = {}
    for line in f:
        tokens = line.split(":")
        key = tokens[0]
        val = int(tokens[1])
        results[key] = val

    f.close()
    return results

filenames = os.listdir(".")
totals = {}
for name in filenames:
    if ".txt" in name:
        results = parse_file(name)
        for k, v in results.items():
            totals[k] = totals.get(k, 0) + v

for k,v in totals.items():
    print "Restaurant '%s' has total %d"%(k, v)
