from termcolor import colored
import pyfiglet
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import os


if os.name == 'nt': 
    os.system('cls')
else:  
    os.system('clear')


result = pyfiglet.figlet_format("Osint / who -> ?")
print(result)
print(colored("me on :", "blue"))
print(colored("   telegram -> @inits5", "yellow"))
print(colored("        Github -> https://github.com/inits5\n", "yellow"))
while True:
    print(colored("1 ->  IP Addresses", "green"))
    print(colored("2 ->  Domains", "green"))

    user_input = input(colored("\nPlease choose a number : ", "light_cyan"))
    
    try:
        int_input = int(user_input)
        
        if int_input == 1:
            print(colored("1 -> VD Port-Scan", 'green', attrs=['bold']))
            print(colored("2 -> VD Whois", 'green', attrs=['bold']))
            print(colored("3 -> VD TraceRoute", 'green', attrs=['bold']))
            user_input_IP = input(colored("\nPlease choose a number : ", "blue"))
            try : 
                IP = int(user_input_IP)
                if IP == 1 :
                    user_input_port = input("Write the ip you want (__exampel__ : 127.0.0.1) : ")
                    async def fetch_port_scan_data(searchDomain):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(f"https://viewdns.info/portscan/?host={searchDomain}") as response:
                                if os.name == 'nt': 
                                    os.system('cls')
                                else:  
                                    os.system('clear')
                                status_message = colored("\nstatus: ", "red")
                                print(status_message + str(response.status)) 
                                html = await response.text()
                                soup = BeautifulSoup(html, 'html.parser')


                        table = soup.find('table', border='1')
                        if not table:
                            result = pyfiglet.figlet_format("o!o")
                            print(result)
                            return

                        rows = table.find_all('tr')[1:]  


                        for row in rows:
                            cols = row.find_all('td')
                            if len(cols) < 3: 
                                continue
                            
                            port = colored(cols[0].text.strip(), "yellow")
                            service = colored(cols[1].text.strip(), "blue")
                            status_img = cols[2].find('img')['src']

                            if 'ok' in status_img:
                                status = colored('open', "green")
                            else:
                                status = colored('closed', "red")

                            print(f"Port: {port}, Service: {service}, Status: {status}")


                    asyncio.run(fetch_port_scan_data(user_input_port))
                elif IP == 2:
                    user_input_whois = input("Write the ip you want (__exampel__ : 127.0.0.1) :")
                    async def fetch_whois_data(searchDomain):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(f"https://viewdns.info/whois/?domain={searchDomain}") as response:
                                if os.name == 'nt': 
                                    os.system('cls')
                                else:  
                                    os.system('clear')
                                status_message = colored("\nstatus: ", "red")
                                print(status_message + str(response.status)) 
                                html = await response.text()
                                soup = BeautifulSoup(html, 'html.parser')
                                whois_info = soup.find('font', face='Courier')
                                if not whois_info:
                                    print(colored("WHOIS information not found!", 'yellow'))
                                    return
                                whois_text = whois_info.get_text(separator="\n").strip()
                                for line in whois_text.splitlines():
                                    line = line.strip()
                                    if "Domain Name:" in line:
                                        print(colored(line, 'green', attrs=['bold']))  
                                    elif "Registrar:" in line or "Creation Date:" in line or "Expiration Date:" in line:
                                        print(colored(line, 'blue', attrs=['bold']))  
                                    elif "REDACTED FOR PRIVACY" in line:
                                        print(colored(line, 'cyan', attrs=['bold']))  
                                    elif "Name Server:" in line:
                                        print(colored(line, 'magenta', attrs=['bold'])) 
                                    elif "Email:" in line or "Phone:" in line or "Fax:" in line:
                                        print(colored(line, 'yellow', attrs=['bold'])) 
                                    elif line == "":
                                        print(colored("undefind", 'grey'))  
                                    else:
                                        print(colored(line, 'grey', attrs=['bold']))  
                    asyncio.run(fetch_whois_data(user_input_whois))
                elif IP == 3:
                    LocateIp = input("Write the ip you want (__exampel__ : 127.0.0.1): ")
                    async def main(searchDomain):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(f"https://viewdns.info/traceroute/?domain={searchDomain}") as response:
                                if os.name == 'nt': 
                                    os.system('cls')
                                else:  
                                    os.system('clear')
                                status_message = colored("\nstatus: ", "red")
                                print(status_message + str(response.status))  
                                html = await response.text()
                                soup = BeautifulSoup(html, 'html.parser')
                                for br in soup.find_all("br"):
                                    br.replace_with("\n")
                                table = soup.find_all("table")[2]
                                result = table.find_all("font")[1]
                                print(colored(result.get_text(),"light_magenta"))
                    asyncio.run(main(LocateIp))
                else:
                    print(colored("chose number 1-3", "red"))
            except ValueError:
                print(colored("only insert number", "red", attrs=["underline", "bold"]))
            break
        elif int_input == 2:
            print(colored("1 -> Reverse Domain", 'green', attrs=['bold']))
            print(colored("2 -> IP history", 'green', attrs=['bold']))
            print(colored("3 -> Subdomain finder", 'green', attrs=['bold']))
            user_input_IP = input(colored("\nPlease choose a number : ", "blue"))
            try:
                IP = int(user_input_IP)
                if IP == 1:
                    user_input_RD = input("Please enter the URL without https/http -> (exampel.com): ")
                    async def fetch_reverse_whois_data(searchDomain):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(f"https://viewdns.info/reversewhois/?q={searchDomain}&t=1") as response:
                                if os.name == 'nt': 
                                    os.system('cls')
                                else:  
                                    os.system('clear')
                                print(colored("Status: ", 'red'), colored(response.status, 'red'))

                                html = await response.text()
                                soup = BeautifulSoup(html, 'html.parser')

                                table = soup.find('table', border='1')
                                if not table:
                                    print(colored("WHOIS information not found!", 'yellow'))
                                    return

                                rows = table.find_all('tr')[1:]

                                headers = table.find_all('td')
                                print(colored(headers[0].text.strip(), 'green', attrs=['bold']),
                                      colored(headers[1].text.strip(), 'blue', attrs=['bold']),
                                      colored(headers[2].text.strip(), 'magenta', attrs=['bold']))

                                for row in rows:
                                    cols = row.find_all('td')
                                    if len(cols) < 3:  
                                        continue
                                    
                                    domain_name = cols[0].text.strip()
                                    creation_date = cols[1].text.strip() if cols[1].text.strip() else "N/A"
                                    registrar = cols[2].text.strip() if cols[2].text.strip() else "N/A"

                                    print(colored(domain_name, 'cyan'), 
                                          colored(creation_date, 'red' if creation_date == "N/A" else 'yellow'), 
                                          colored(registrar, 'red' if registrar == "N/A" else 'blue'))

                    asyncio.run(fetch_reverse_whois_data(user_input_RD))
                elif IP == 2:
                    user_input_IH = input("Please enter the URL without https/http -> (exampel.com): ")
                    async def fetch_ip_history_data(searchDomain):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(f"https://viewdns.info/iphistory/?domain={searchDomain}") as response:
                                if os.name == 'nt': 
                                    os.system('cls')
                                else:  
                                    os.system('clear')
                                print(colored("Status: ", 'red'), colored(response.status, 'red'))

                                html = await response.text()
                                soup = BeautifulSoup(html, 'html.parser')


                                table = soup.find('table', border='1')
                                if not table:
                                    print(colored("IP history information not found!", 'yellow'))
                                    return

                                rows = table.find_all('tr')[1:]  


                                headers = table.find_all('td')
                                print(colored(headers[0].text.strip(), 'green', attrs=['bold']),
                                      colored(headers[1].text.strip(), 'blue', attrs=['bold']),
                                      colored(headers[2].text.strip(), 'magenta', attrs=['bold']),
                                      colored(headers[3].text.strip(), 'cyan', attrs=['bold']))


                                for row in rows:
                                    cols = row.find_all('td')
                                    if len(cols) < 4: 
                                        continue
                                    
                                    ip_address = cols[0].text.strip()
                                    location = cols[1].text.strip() if cols[1].text.strip() else "N/A"
                                    ip_owner = cols[2].text.strip() if cols[2].text.strip() else "N/A"
                                    last_seen = cols[3].text.strip() if cols[3].text.strip() else "N/A"


                                    print(colored(ip_address, 'cyan'), 
                                          colored(location, 'red' if location == "N/A" else 'yellow'), 
                                          colored(ip_owner, 'red' if ip_owner == "N/A" else 'blue'),
                                          colored(last_seen, 'red' if last_seen == "N/A" else 'yellow'))

                    asyncio.run(fetch_ip_history_data(user_input_IH))
                elif IP == 3:
                    
                    async def fetch_subdomains(domain):
                        url = f"https://crt.sh/?q=.{domain}&output=json"
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url) as response:
                                data = await response.text()
                                return json.loads(data)

                    async def get_sorted_subdomains(domain):
                        jobj = await fetch_subdomains(domain)
                        subs = [entry['common_name'] for entry in jobj]
                        subs = sorted(set(subs))
                        return subs

                    def print_colored_subdomains(subdomains):
                        for sub in subdomains:
                            print(colored(sub, 'cyan', attrs=['bold']))


                    domain_to_search = input("Please enter the URL without https/http -> (exampel.com) : ")
                    print(colored("please wait ...", "light_green"))
                    sorted_subdomains = asyncio.run(get_sorted_subdomains(domain_to_search))

                    print(colored("\nSubdomains found:", 'green', attrs=['bold']))
                    print_colored_subdomains(sorted_subdomains)
            except ValueError:
                print(colored("only insert number", "red", attrs=["underline", "bold"]))
            
            break  
        else:
            print("only is number\n")
    
    except ValueError:
        print("only insert number\n")
