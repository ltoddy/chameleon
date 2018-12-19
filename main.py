import asyncore

from chameleon import Chameleon

if __name__ == '__main__':
    server = Chameleon()
    print("server run at 127.0.0.1:1025\n")
    asyncore.loop()
