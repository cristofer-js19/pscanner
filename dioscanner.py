import nmap
import re

scanner = nmap.PortScanner()

print("Welcome to the DIOScanner")

ip = input("Enter the IP to be verified: ")
pattern = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
if not pattern.match(ip):
    print("Invalid IP...")
    quit()

print("The IP informed was:", ip)

menu = input("""\nPlease, choose the verification type:
                1 -> SYN Type
                2 -> UDP Type
                3 -> Comprehensive Type
                Type the chosen option: """)
print("The chosen option was:", menu)


def execute_verification(verification_var, verification_type):
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', verification_var)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Opened Doors: ", scanner[ip][verification_type].keys())


if menu == "1":
    execute_verification('-v -sS', 'tcp')
elif menu == "2":
    execute_verification('-v -sU', 'udp')
elif menu == "3":
    execute_verification('-v -sC', 'tcp')
else:
    print("Please, choose a valid option.")
