import pymem
import socket
import time
import sys

# Config
HOST = '192.168.2.107'
PORT = 1339
last_score = 0
offsets = [0x233D968, 0x88, 0xC0, 0x8, 0x238, 0x40, 0x80, 0x4FC]
pymem.logger.disabled = True
pymem.process.logger.disabled = True


def get_address():
    # Starts pymem class with rocket league process
    try:
        global pm
        pm = pymem.Pymem('RocketLeague.exe')
    except pymem.exception.ProcessNotFound or pymem.exception.CouldNotOpenProcess:
        print("Could not open process")
        input("Press any button to exit")
        sys.exit(-1)

    # Uses pointer offsets to find correct memory address of goals
    try:
        ptr = pm.process_base.lpBaseOfDll
        for off in offsets:
            ptr = ptr + off
            if off is not offsets[-1]:
                ptr = int.from_bytes(pm.read_bytes(ptr, 8), 'little')
    except Exception as e:
        print("excepted")
        return None

    return ptr


def main():
    while True:
        global last_score
        address = None
        while not address:
            address = get_address()
            time.sleep(2)
        print(f"Starting! Addr: {hex(address)}")
        while True:
            try:
                score = pm.read_int(address)
                if score < 0 or score >= 10:
                    last_score = 0
                    break
            except Exception:
                last_score = 0
                break
            if score != last_score:
                last_score += 1
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.connect((HOST, PORT))
                    msg = 'goal'
                    print("GOAL!")
                    client.send(msg.encode())
                time.sleep(7)
            last_score = score
            time.sleep(0.1)


if __name__ == '__main__':
    main()
