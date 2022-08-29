import os
import sys
import utils

forced_retest_list = ["checker.py", "gen.py"]
trigger_retest_dirs = ["data-gen", "std", "data-gen/input"]
trigger_repack_dirs = trigger_retest_dirs + ["docs"]


def getprobs(for_pack):
    changed_problems = set()
    with open("./changed-files.txt", "r") as f:
        for x in f.readlines():
            dir = os.path.dirname(x)
            if for_pack:
                dirs = trigger_repack_dirs
            else:
                dirs = trigger_retest_dirs
            for d in dirs:
                if dir.endswith(d):
                    changed_problems.add(dir.split("/")[-1 - len(d.split("/"))])
                    break
            if str(x).strip() in forced_retest_list:
                os.system("echo forced retest")
                for p in os.listdir("./problems"):
                    changed_problems.add(p.split("/")[-1])
                return changed_problems

    return changed_problems


if __name__ == "__main__":

    changed_problems = getprobs(False)
    os.system("echo \"changed problems: {}\"".format(str(changed_problems)))

    with open("changed-probs.txt", "w") as w:
        w.write(" ".join([x for x in changed_problems]))

    with open("changed-probs-for-pack.txt", "w") as w:
        cp = getprobs(True)
        os.system("echo \"changed problems for pack: {}\"".format(str(cp)))
        w.write(" ".join([x for x in cp]))

    for p in changed_problems:
        os.environ['CUR_PROB'] = p
        os.system("echo start test:{}".format(p))
        utils.execute("python3 checker.py")
