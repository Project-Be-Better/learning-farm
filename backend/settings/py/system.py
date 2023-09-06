from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%d/%m/%Y-%H:%M:%S")
formatted_date_DMY = now.strftime("%d-/%m-/%Y")


class Paths:
    LOGS = f"logs/{formatted_date}-log.log"
