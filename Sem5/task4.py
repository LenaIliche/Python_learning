def encode_rle(s):
    res = ""
    i = 0
    while i <= len(s) - 1:
        count = 1
        ch = s[i]
        j = i
        while j < len(s) - 1:
            if s[j] == s[j + 1]:
                count += 1
                j += 1
            else:
                break
        res += str(count if count != 1 else "") + ch
        i = j + 1
    return res


s = "lolkek cheburek lllllooooollllkeeeeeek ccccheeeeeeeeeeeeburekkkkkkkk"

print(encode_rle(s))
