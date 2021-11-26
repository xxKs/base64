import base64
print ("Welcome")
encoded = input("paste your encodedStr Here")
decodedStr = base64.urlsafe_b64decode(encoded)
decodedStr1 = str(decodedStr, "UTF-8")

print("----> Here is your decodedStr")
print("------------")
print(decodedStr1)