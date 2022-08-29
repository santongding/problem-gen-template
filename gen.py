import os
import sys
import utils

proj = os.environ.get("CUR_PROB")
data_gen_dir = "./problems/{}/data-gen".format(proj)
sys.path.append(data_gen_dir)

import validator


def gen(outputDir):
    dconfigPath = "./problems/{}/data-gen/gen-config.csv".format(proj)

    with open(dconfigPath, "r") as f:
        f.readline()
        ids = [x.split(",")[0].lstrip() for x in f.readlines()]

    for i in ids:
        os.system("echo Start gen " + str(i))
        param = utils.readparam(data_gen_dir, int(i))
        file = "{}/{}.in".format(outputDir, i)
        with open(file, "w") as sys.stdout:
            if param.is_static == 1:
                with open(data_gen_dir + "/input/{}.in".format(param.data_id)) as f:
                    print("\n".join([x.strip() for x in f.readlines() if len(x.strip()) > 0]))
            else:
                import data_gen
                data_gen.gen_data(param)

        with open(file, "r") as sys.stdin:
            validator.validate(param, utils)
