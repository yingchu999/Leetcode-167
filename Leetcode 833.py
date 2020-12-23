for index, source, target in sorted(zip(indexes, sources, targets), reverse = True):
    if index + len(source) <= len(S) and S[index:index+len(source)] == source:
        S = S[:index] + target + S[index+len(source):]
return S
