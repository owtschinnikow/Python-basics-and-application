"""
Tue May 29 00:21:08 2018: msg1
Tue May 29 00:21:08 2018: msg2
['msg1', 'msg2']

Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при
добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из
только что добавленного элемента.
"""

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        return self.log(elem)

def main():
    a = LoggableList()
    a.append('msg 1')
    a.append('msg 2')
    print(a)

if __name__ == '__main__':
    main()
