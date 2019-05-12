import string
import 凯撒加密
def kaisa(s,k):
    print("原码：",s)
    s=凯撒加密.kaisa(s,k)
    print("加密：",s)
    k=26-k
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    befor=string.ascii_letters
    after=lower[k:]+lower[:k]+upper[k:]+upper[:k]
    table=''.maketrans(befor,after)
    return s.translate(table)
if __name__=='__main__':
    print("解密：",kaisa("woxihuanwoziji",4))
