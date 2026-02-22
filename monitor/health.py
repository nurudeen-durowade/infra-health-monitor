import psutil

def check_cpu():
    return psutil.cpu_percent(interval=1)


def check_memory():
    return psutil.virtual_memory().percent


def check_disk():
    return psutil.disk_usage('/').percent

output_file='../../logs/health.log'

def write_to_logs():
    with open (output_file, 'w') as f:
        print(f"CPU Usage is: {check_cpu}%", file=f)
        print(f"Disk Usage is: {check_disk}%", file=f)
        print(f"Memory Usage is: {check_memory}", file=f)