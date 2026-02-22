import psutil

print("Starting Infra health Monitor ... \n")


output_file = './logs/health.log'

#Get CPU percentage

cpu_usage = psutil.cpu_percent(interval=1)

# Get Disk Usage
disk_usage = psutil.disk_usage('/').percent


#Get Memory Usage
memory_usage = psutil.virtual_memory().percent

#Save to a log file
with open (output_file, 'w') as f:
    print(f"CPU Usage is: {cpu_usage}%", file=f)
    print(f"Disk Usage is: {disk_usage}%", file=f)
    print(f"Memory Usage is: {memory_usage}", file=f)

# What if cpu > 80% ?
# Add a check

if cpu_usage > 80:
    print("WARNING: High CPU usage detected!")