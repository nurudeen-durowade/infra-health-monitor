from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, ALERT_CHANNEL


def cpu_alert(cpu_usage):
    if cpu_usage > CPU_THRESHOLD:
        send_slack_alert(f"CPU usage high: {cpu_usage}%")
        send_email_alert(f"CPU usage high: {cpu_usage}%")
        pass

def memory_alert(memory_usage):
    if memory_usage > MEMORY_THRESHOLD:
        send_slack_alert(f"CPU usage high: {memory_usage}%")
        send_email_alert(f"CPU usage high: {memory_usage}%")
        pass

def disk_alert(disk_usage):
    if disk_usage > DISK_THRESHOLD:
        send_slack_alert(f"CPU usage high: {disk_usage}%")
        send_email_alert(f"CPU usage high: {disk_usage}%")
        pass