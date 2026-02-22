import psutil

import os
import random

def check_cpu(simulate=False):
    if simulate:
        return random.randint(80, 99)
    return psutil.cpu_percent(interval=1)


def check_memory(simulate=False):
    if simulate:
       return random.randint(89, 99)
    return psutil.virtual_memory().percent


def check_disk(simulate=False):
    if simulate:
       return random.randint(89, 99)
    return psutil.disk_usage('/').percent


output_file='./logs/health.log'


os.makedirs(os.path.dirname(output_file), exist_ok=True)

def write_to_logs(cpu, memory, disk):
    with open (output_file, 'w') as f:
        print(f"CPU Usage is: {cpu}%", file=f)
        print(f"Disk Usage is: {disk}%", file=f)
        print(f"Memory Usage is: {memory}%", file=f)

if __name__ == "__main__":
    write_to_logs(simulate=True)
    print(f"Simulated health metrics written to {output_file}")
