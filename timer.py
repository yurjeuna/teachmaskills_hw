import winsound
import time

def is_ok(i):
    if i == '-' or i == '0' or i == '00':
        return 0
    else:
        try:
            i = int(i)
            return i
        except ValueError:
            print('Ooops! Incorrect format. Do it again!')
            return -1

while True:
    timer = input("Enter timer in format hours:minutes:seconds: -:-:- ").split(':')
    whole = 0
    if is_ok(timer[0]) == -1:
        continue
    else:
        whole = is_ok(timer[0]) * 3600
    if is_ok(timer[1]) == -1:
        continue
    else:
        whole += (is_ok(timer[1]) * 60)
    if is_ok(timer[2]) == -1:
        continue
    else:
        whole += is_ok(timer[2])
        break

time.sleep(int(whole))
print('Alarm!')
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
