import sys
import redis

def connect_redis():
    return redis.Redis(host='redis', port=6379, db=0)

client = connect_redis()
if client.ping():
    print('CONNECTED TO REDIS...')

    while True:
        try:
            cmd = sys.stdin.readline().strip()
            
            if cmd != '':
                if cmd[:3] == 'set':
                    key = cmd.split()[1]
                    value = cmd.split()[2]
                    client.set(key, value)
                    print(f"Value has been set for key: {key} and value: {value}\n\n")
                elif cmd[:3] == 'get':
                    key = cmd.split()[1]
                    value = client.get(key)
                    print(f"Value for key: {key} is {value}\n\n")
            else:
                print('No command entered...\n\n')
                exit()
        except Exception as e:
            print(f"ERROR: {e}\n\n")

else:
    print('ERROR CONNECTING TO REDIS...')