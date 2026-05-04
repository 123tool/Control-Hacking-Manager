#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYSTEM: 123TOOLHACK v3.0
DEVELOPER: SPY-E
PLATFORM: Ubuntu/Xubuntu/Kali/Termux
DESCRIPTION: Hacking Toolkits Manager
"""

import os
import json
import time
import sys
from colorama import Fore, Style, init
from core.ui import banner, clear
from core.engine import ToolEngine

# Inisialisasi Colorama untuk warna terminal
init(autoreset=True)

def load_db():
    """Memuat database tools dari file JSON"""
    try:
        with open('data/registry.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Database data/registry.json tidak ditemukan!")
        sys.exit()
    except json.JSONDecodeError:
        print(f"{Fore.RED}[!] Format JSON di data/registry.json rusak!")
        sys.exit()

def display_menu(db):
    """Menampilkan menu dalam format grid dua kolom yang rapi"""
    items = list(db.items())
    print(f"{Fore.WHITE}{'='*85}")
    
    # Render menu secara dinamis (50+ tools)
    for i in range(0, len(items), 2):
        k1, v1 = items[i]
        # Membatasi nama agar tidak merusak layout kolom
        name1 = (v1['name'][:28] + '..') if len(v1['name']) > 28 else v1['name']
        col1 = f"{Fore.CYAN}[{k1}] {Fore.WHITE}{name1}".ljust(45)
        
        col2 = ""
        if i + 1 < len(items):
            k2, v2 = items[i+1]
            name2 = (v2['name'][:28] + '..') if len(v2['name']) > 28 else v2['name']
            col2 = f"{Fore.CYAN}[{k2}] {Fore.WHITE}{name2}"
        
        print(f"{col1}{col2}")
    
    print(f"{Fore.WHITE}{'='*85}")
    print(f"{Fore.RED}[00] EXIT SYSTEM")
    print(f"{Fore.RED}{'='*85}")

def run():
    """Fungsi utama untuk menjalankan program"""
    engine = ToolEngine()
    db = load_db()

    while True:
        clear()
        banner() # Memanggil banner 123TOOLHACK by SPY-E
        display_menu(db)
        
        try:
            # Input navigasi
            choice = input(f"{Fore.YELLOW}Select the number: {Fore.WHITE}").strip()
            
            # Logika Exit
            if choice == "00" or choice == "0":
                print(f"\n{Fore.RED}[!] SHUTTING DOWN SYSTEM...")
                time.sleep(1)
                break
                
            # Logika Eksekusi Tool
            if choice in db or choice.zfill(2) in db:
                key = choice if choice in db else choice.zfill(2)
                tool_name = db[key]['name']
                tool_cmd = db[key]['cmd']
                
                engine.execute(tool_cmd, tool_name)
                input(f"\n{Fore.GREEN}Execution finished. Press [ENTER] to return...")
            else:
                if choice != "":
                    print(f"{Fore.RED}[!] Pilihan '{choice}' tidak terdaftar di sistem!")
                    time.sleep(1.5)
                    
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}[!] SYSTEM INTERRUPTED BY USER. EXITING...")
            sys.exit()

if __name__ == "__main__":
    # Menjalankan aplikasi
    run()
