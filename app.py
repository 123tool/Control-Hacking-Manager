import json
import time
from core.ui import banner, clear
from core.engine import ToolEngine
from colorama import Fore, Style, init

init(autoreset=True)

def load_db():
    with open('data/registry.json', 'r') as f:
        return json.load(f)

def run():
    engine = ToolEngine()
    db = load_db()

    while True:
        clear()
        banner()
        
        # Render Menu Dua Kolom (Estetika Pro)
        items = list(db.items())
        for i in range(0, len(items), 2):
            k1, v1 = items[i]
            col1 = f"{Fore.CYAN}[{k1}] {Fore.WHITE}{v1['name']}".ljust(40)
            col2 = ""
            if i + 1 < len(items):
                k2, v2 = items[i+1]
                col2 = f"{Fore.CYAN}[{k2}] {Fore.WHITE}{v2['name']}"
            print(f"{col1}{col2}")

        print(f"\n{Fore.RED}[00] EXIT SYSTEM")
        print(f"{Fore.RED}------------------------------------------------------------------------------------------")
        
        try:
            choice = input(f"{Fore.CYAN}Select the number: {Fore.WHITE}").strip()
            
            if choice == "00":
                print(f"{Fore.YELLOW}[!] SHUTTING DOWN...")
                break
                
            if choice in db:
                engine.execute(db[choice]['cmd'], db[choice]['name'])
                input(f"\n{Fore.GREEN}Press [ENTER] to return...")
            else:
                print(f"{Fore.RED}[!] INVALID SELECTION.")
                time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run()
