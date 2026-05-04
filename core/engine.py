import os
import sys
import subprocess
from colorama import Fore

class ToolEngine:
    def __init__(self):
        self.platform = self._detect_platform()

    def _detect_platform(self):
        # Deteksi apakah berjalan di lingkungan Termux atau Linux biasa
        if os.path.exists('/data/data/com.termux'):
            return "termux"
        return "linux"

    def execute(self, command, name):
        print(f"\n{Fore.YELLOW}[!] INITIALIZING: {name}...")
        
        # Penyesuaian perintah otomatis
        if self.platform == "termux":
            # Hapus sudo dan ganti apt ke pkg untuk Termux
            cmd = command.replace("sudo ", "").replace("apt ", "pkg ")
        else:
            # Pastikan perintah apt menggunakan sudo di Ubuntu/Linux
            if "apt" in command and not command.startswith("sudo"):
                cmd = f"sudo {command}"
            else:
                cmd = command

        try:
            # Eksekusi sistem dengan output real-time
            subprocess.run(cmd, shell=True, check=True)
            print(f"{Fore.GREEN}[+] SUCCESS: {name} terpasang.")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[x] CRITICAL ERROR: Gagal mengeksekusi {name}.")
        except Exception as e:
            print(f"{Fore.RED}[x] UNEXPECTED ERROR: {str(e)}")
