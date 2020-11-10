# Program to block websites

hosts_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_ip = "127.0.0.1"
website = str(input("Enter the website you want to block : "))

with open(hosts_path, 'r+') as file:
    cont = file.read()
    if website in cont:
        print("Website is already blocked.\n")
        pass
    else:
        file.write(redirect_ip + "\t" + website + "\n")
        print("Website blocked.\n")

