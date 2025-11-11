import os
import shutil
import socket

def main():
    mappe()

    fil = open(f"C:/maskin/{socket.gethostname()}.txt", "w")
    fil.write(f"{operativsystem()["operativsystemet"]}\n")
    fil.write(f"{operativsystem()["versjon"]}\n")
    fil.write(f"{Disk()}\n")
    fil.write(f"{bruker()}\n")
    fil.write(f"{finnIp()}\n")
    fil.write(f"{henteApper()}\n")

def operativsystem():
    match os.name:
        case "nt":
            operativsystemet = "Windows"
        case "posix":
            operativsystemet = "Linux"
        case "java":
            operativsystemet = "Java"

    try:
        versjon = os.popen("ver").read().strip()
    except:
        versjon = "versjon er ikke tilgjengelig"
    return {"operativsystemet":operativsystemet, "versjon":versjon}



def Disk():
    giga = 1024 * 1024 * 1024

    match os.name:
        case "nt": 
            total, brukt, ledig = shutil.disk_usage("C:\\")
        case "posix":
           total, brukt, ledig = shutil.disk_usage("/")
        case _:
            print("Ukjent OS-type")
    return f"{ledig / giga:.2f}"


def bruker():
    return os.getlogin()

def finnIp():
    result = ""
    if os.name == "nt":
        result = os.popen("ipconfig").read()
    else:
        result = os.popen("ifconfig").read()
    return result

if __name__ == '__main__':
    main()