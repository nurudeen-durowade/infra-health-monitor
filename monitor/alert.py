from .config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, SLACK_WEBHOOK_URL
import smtplib,ssl
import requests
from email.mime.text import MIMEText
from email.message import EmailMessage
import os



def send_email_alert(subject: str, message: str, simulate=False):

    if simulate:
        print(f"[SIMULATION] Email: {subject} -> {recipient}")
        return

    # Example using Gmail SMTP

    sender_email = os.getenv("EMAIL_USER")

    sender_password = os.getenv("EMAIL_PASSWORD")

    recipient = os.getenv("EMAIL_RECIPIENT")

    #msg = MIMEText(message)

    msg = EmailMessage()

    msg['Subject'] = subject

    msg['From'] = sender_email

    msg['To'] = recipient

    msg.set_content(message)


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            #server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email successfully sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        return



def send_slack_alert(message: str, simulate=False):
    if simulate:
        print(f"[SIMULATION] Slack: {message}")
        return

    try:
        payload = {
            "text": message
        }
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)

        if response.status_code == 200:
            print("Slack alert sent successfully")
        else:
            print(f"Failed to send Slack alert: {response.text}")
    except Exception as e:
        print(f"Failed to send slack alert: {e}")









def usage_alert(cpu_usage, memory_usage, disk_usage, simulate=False):
    if (cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD or disk_usage > DISK_THRESHOLD) :
                subject = f"[ALERT] Application Server Resource Usage"
                body = f"""
Attention,

The infra-health-monitor detected high Resource usage.

CPU Usage: {cpu_usage}%
Memory Usage: {memory_usage}%
Disk Usage: {disk_usage}%

Please take necessary action.

- Infra Health Monitor
"""
                send_slack_alert(f"Resource usage is high: CPU:{cpu_usage}%,  MEMORY: {memory_usage}%,  DISK: {disk_usage}", simulate)
                send_email_alert(subject, body, simulate)
        

# def memory_alert(memory_usage, simulate=False):
#     if memory_usage > MEMORY_THRESHOLD:
#         send_slack_alert(f"Memory usage high: {memory_usage}%", simulate)
#         send_email_alert(f"Memory usage high: {memory_usage}%",  f"Memory usage is {memory_usage}%", simulate)
        

# def disk_alert(disk_usage, simulate=False):
#     if disk_usage > DISK_THRESHOLD:
#         send_slack_alert(f"Disk usage high: {disk_usage}%", simulate)
#         send_email_alert(f"Disk usage high: {disk_usage}%", f"Memory usage is {disk_usage}%", simulate)
        