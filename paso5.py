while True:
    aclNum = input("Ingrese el numero de ACL IPV4 o escriba exit para salir: ")

    if aclNum.lower() == "exit":
        break

    if aclNum.isdigit() and int(aclNum) >= 1 and int(aclNum) <= 99:
        print("Este es un ACL IPv4 estándar.")
    elif aclNum.isdigit() and int(aclNum) >=100 and int(aclNum) <= 199:
        print("Este es una ACL IPv4 extendida")
    else:
        print("Esta no es una ACL .")
