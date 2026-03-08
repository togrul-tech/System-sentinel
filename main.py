import psutil
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)


def print_gauge(label, percent, color):
    """Faiz göstəricisi üçün vizual bar yaradır."""
    bar_length = 20
    filled_length = int(bar_length * percent / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"{Fore.WHITE}{label:<10} [{color}{bar}{Fore.WHITE}] {percent}%")


def monitor_system():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.CYAN}{Style.BRIGHT}🛡️  SYSTEM SENTINEL - REAL-TIME MONITOR")
            print(f"{Fore.WHITE}------------------------------------------")

            # CPU Info
            cpu_usage = psutil.cpu_percent(interval=None)
            print_gauge("CPU Usage", cpu_usage, Fore.GREEN if cpu_usage < 70 else Fore.RED)

            # Memory Info
            memory = psutil.virtual_memory()
            print_gauge("RAM Usage", memory.percent, Fore.YELLOW)

            # Disk Info
            disk = psutil.disk_usage('/')
            print_gauge("Disk Space", disk.percent, Fore.MAGENTA)

            # Network Speed (Simple version)
            net = psutil.net_io_counters()
            print(f"\n{Fore.BLUE}🌐 Network Sent: {net.bytes_sent // 1024} KB")
            print(f"{Fore.BLUE}🌐 Network Recv: {net.bytes_recv // 1024} KB")

            print(f"\n{Fore.WHITE}Press Ctrl+C to exit...")
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Sentinel stopped.")


if __name__ == "__main__":
    monitor_system()
