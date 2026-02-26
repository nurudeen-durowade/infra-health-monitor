from monitor import health, alert

import time



while True:
    cpu = health.check_cpu(simulate=True)

    memory = health.check_memory(simulate=True)

    disk = health.check_disk(simulate=True)

    health.write_to_logs(cpu, memory, disk)

    alert.usage_alert(cpu, memory, disk, simulate=False)

    # alert.memory_alert(memory, simulate=False)

    # alert.disk_alert(disk, simulate=False)

    time.sleep(60)


