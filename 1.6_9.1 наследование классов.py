
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))



if __name__ == '__main__':
    test()
    # main()
