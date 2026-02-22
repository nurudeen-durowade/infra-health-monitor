from monitor import health, alert

import time



while True:
    cpu = health.check_cpu()

    memory = health.check_memory()

    disk = health.check_disk()

    health.write_to_logs()

    alert.cpu_alert(cpu)

    alert.memory_alert(memory)

    alert.disk_alert(disk)

