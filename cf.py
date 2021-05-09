import pyaes
import base64

key = "d8cg8gVakEq9Agup".encode('utf8')

def enc(msg,key=key):
    encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationECB(key))
    ciphertext = encrypter.feed(msg.encode('utf8'))
    ciphertext += encrypter.feed()
    return base64.b64encode(ciphertext).decode('utf8')

# We can decrypt the cipher text in chunks (here we split it in half)
def dec(msg,key=key):
    msg = base64.b64decode(msg)
    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationECB(key))
    decrypted = decrypter.feed(msg)
    decrypted += decrypter.feed()
    return decrypted.decode('utf8')

if __name__ == "__main__":
    data = "logId=g6sChrM2VMf2iGWPgTpErwaRhnZGNLzjMuo3p5rH4T6egh5bz9Mhe%2Fw%2BtKRGL9RH&lessonLocation=mKfpYqk7vssAjySbv8BFUw%3D%3D&studyTime=sdTUOdlLMF1ueh07yda1dA%3D%3D&resourceTotalTime=4ftcAHDfVeKQahFVgbNvyw%3D%3D&organizationId=jlDaqecOmjPJ68pDFUKOZqPk2c0%2Bldukax%2FXqDpjx9IHUGJoO5w%2FHU8ZKLtgLctN&entrance=uMpvW9kR%2Fvroc%2Bt5cdycQg%3D%3D&singleMark=hsaMC8OKjjdwLILsBONtlP8lZP5EY3GXQGCJ3iHAgS9uiMI9UPiHyTg%2BWTqK8qqU"
    from urllib.parse import parse_qs,parse_qsl, urlencode

    qs = parse_qsl(data)
    qs_d = parse_qs(data)
    qs_new = []
    for key, value in qs:
        if "studyTime" in key or "lessonLocation" in key:
            qs_new.append((key,enc(str(int(dec(qs_d["resourceTotalTime"][0]))-10))))
        else:
            qs_new.append((key,value))
    print('-----')
    for (key, value),(k2,v2) in zip(qs_new,qs):
        print("\tget %s: %s (%s)->%s (%s)" % (key,dec(v2),v2,dec(value),value))

