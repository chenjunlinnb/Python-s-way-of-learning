import string
def kaisa(s,k):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    befor=string.ascii_letters
    after=lower[k:]+lower[:k]+upper[k:]+upper[:k]
    table=''.maketrans(befor,after)
    return s.translate(table)
if __name__ == '__main__':
    print("加密：",kaisa("woxihuanwoziji",4))
