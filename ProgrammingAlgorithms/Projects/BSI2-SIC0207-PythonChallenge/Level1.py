# Level 1
print(2**38)

# Leve 2
intab = "abcdefghijklmnopqrstuvwxyz .()"
outtab = "cdefghijklmnopqrstuvwxyzab .()"
translation = str.maketrans(intab, outtab)

txt = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmglegr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
print(txt.translate(translation))
