import os
import sys
import gen
import utils

execute = utils.execute


def buildCpp(stdDir):
    stdPath = ""
    exePaths = []
    for x in os.listdir(stdDir):
        p = stdDir + "/" + x
        execute("g++ -o ./temp/{} -O2 -std=c++17 {}".format(x.split(".")[0], p))
        f = "./temp/{}".format(x.split(".")[0])
        if x == "std.cpp":
            stdPath = f

        exePaths.append(f)

    return stdPath, exePaths


def test(cpps, dataPath, outputDir):
    os.system("echo start test: {}".format(dataPath))
    outputName = dataPath.split("/")[-1].split(".")[0] + ".out"
    outputPath = outputDir + "/" + outputName

    execute("./{} > {} < {}".format(cpps[0], outputPath, dataPath), 1.0)

    for c in cpps[1]:
        cname = c.split("/")[-1]
        if len(cname.split('_')) > 1:
            execute("./{} >./temp/temp.out <{}".format(c, dataPath), float(cname.split('_')[-1]))
        else:
            execute("./{} >./temp/temp.out <{}".format(c, dataPath), 1.0)
        try:
            execute("diff ./temp/temp.out {}".format(outputPath))
        except Exception as e:
            execute("cat {}".format(dataPath))
            exit(1)
            pass


if __name__ == "__main__":
    if len(sys.argv) != 1:
        utils.err("arg num not correct")

    proj = os.environ.get("CUR_PROB")

    dconfigPath = "./problems/{}/data-gen/gen-config.csv".format(proj)
    stdDir = "./problems/{}/std/".format(proj)
    validatorPath = "./problems/{}/data-gen/validator.py".format(proj)
    dataDir = "./temp/data"
    execute("rm -rf ./temp")
    execute("mkdir ./temp")
    execute("mkdir ./temp/data")
    with open(dconfigPath, "r") as f:
        f.readline()
        ids = [x.split(",")[0].lstrip() for x in f.readlines()]

    gen.gen(dataDir)
    cpps = buildCpp(stdDir)

    datas = [x for x in os.listdir(dataDir)]
    datas.sort()
    for x in datas:
        p = dataDir + "/" + x
        test(cpps, p, dataDir)
