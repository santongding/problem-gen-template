import sys
import os
import multiprocessing


def err(s):
    os.system("echo {}".format(s))
    raise Exception("fail to execute")


def worker(cmd):
    execute(cmd)


def execute(cmd, timeout=None):
    os.system("echo \"_________________{} {} _________________________\"".format("execute", cmd))
    if timeout is None:
        if os.system(cmd) != 0:
            err("fail to execute \"{}\"".format(cmd))
    else:

        process = multiprocessing.Process(target=worker, args=(cmd,))
        process.start()

        process.join(timeout)
        if process.is_alive():
            process.kill()
            err("cmd running over {} secs".format(timeout))

        if process.exitcode != 0:
            raise Exception("fail to execute")


def getints(num):
    assert type(num) == int
    ans = [int(x) for x in input().split()]
    assert len(ans) == num
    return ans


def readparam(cur_path, i):
    with open(cur_path + "/gen-config.csv", "r") as f:
        header = [s.strip() for s in f.readline().split(",")]
        for x in f.readlines():
            lis = [int(s.strip()) for s in x.split(",")]
            if lis[0] == i:
                return DictToObject(dict(zip(header, lis)))


class DictToObject(dict):
    def __init__(self, dic):
        dict.__init__(self)
        for key, item in dic.items():
            if key[0] != '_':
                if type(item) == dict:
                    self.__setattr__(key, DictToObject(item))
                if type(item) == list:
                    self.__setattr__(key, self.__iterlist__(item))
                else:
                    self.__setattr__(key, item)

    # 自定义的一个递归方法，用来将list内的dict元素也转为该类
    def __iterlist__(self, item):
        temp = [DictToObject(x) if type(x) == dict else x for x in item]
        temp = [self.__iterlist__(x) if type(x) == list else x for x in temp]
        return temp

    # 当类进行"."来访问属性时会调用该方法
    def __setattr__(self, key, item):
        dict.__setattr__(self, key, item)
        # 用__dict__来更新该类本身的值
        self.update(self.__dict__)
