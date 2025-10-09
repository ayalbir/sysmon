import psutil
import time

def display_usage(cpu_usage, memory_usage, bars=50):
    cpu_percent = cpu_usage / 100.0
    cpu_bars = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    memory_percent = memory_usage / 100.0
    memory_bars = '█' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))
    
    print(f"\rCPU Usage: |{cpu_bars}| {cpu_usage:.2f}%  ", end='')
    print(f"Memory Usage: |{memory_bars}| {memory_usage:.2f}%", end='\r')
    

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(1)