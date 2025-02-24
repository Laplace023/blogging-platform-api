from datetime import datetime

#INFO: Fetches the current date and time, reusable function for my API calls
def timeNow():
    CurTime = datetime.now()
    time = CurTime.strftime("%m/%d/%Y %H:%M")
    return time

if __name__ == "__main__":
    now = timeNow()
    print(now)
