from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, EMAIL_RECIPIENT, SLACK_WEBHOOK_URL
import smtplib,ssl
import requests
from email.mime.text import MIMEText
from email.message import EmailMessage



def send_email_alert(subject: str, message: str):

    # Example using Gmail SMTP

    sender_email = "nurudeendurowade@gmail.com"

    sender_password = "Durowad8*@123"

    msg = MIMEText(message)

    msg['Subject'] = subject

    msg['From'] = sender_email

    msg['To'] = EMAIL_RECIPIENT


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email successfully sent to {EMAIL_RECIPIENT}")
    except Exception as e:
        print(f"Failed to send email: {e}")



def send_slack_alert(message: str):

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









def cpu_alert(cpu_usage):
    if cpu_usage > CPU_THRESHOLD:
        send_slack_alert(f"CPU usage high: {cpu_usage}%")
        send_email_alert(f"CPU usage high: {cpu_usage}%")
        

def memory_alert(memory_usage):
    if memory_usage > MEMORY_THRESHOLD:
        send_slack_alert(f"CPU usage high: {memory_usage}%")
        send_email_alert(f"CPU usage high: {memory_usage}%")
        

def disk_alert(disk_usage):
    if disk_usage > DISK_THRESHOLD:
        send_slack_alert(f"CPU usage high: {disk_usage}%")
        send_email_alert(f"CPU usage high: {disk_usage}%")
        