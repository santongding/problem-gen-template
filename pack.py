import utils
import os
import sys

need_repack_list = ["pack.py", "pack-config"]

if __name__ == "__main__":
    need_pack = False

    with open("changed-files.txt", "r") as r:  # check if config changed
        lines = [line.strip() for line in r.readlines()]
        for x in need_repack_list:
            if x in lines:
                need_pack = True
                break

    with open("pack-config.txt", "r") as r:  # read config
        dic = eval(r.read())
        config = utils.DictToObject(dic)

    for pack_prob in sys.argv[1:]:  # check if problems changed
        if pack_prob in config.pack_probs_list:
            need_pack = True
            break

    if need_pack:
        filepath = "./temp-package"
        utils.execute("rm -rf {}".format(filepath))
        os.mkdir(filepath)
        for k, v in config.pack_probs_list.items():
            out_dir = "./temp-package/" + v
            os.environ['CUR_PROB'] = k
            utils.execute("python3 checker.py")
            in_dir = "./problems/{}".format(k)
            utils.execute("cp -r {0}/docs {1} || mkdir {1}".format(in_dir, out_dir))
            utils.execute("cp -r {}/std {}/{}".format(in_dir, out_dir, config.std_dir_name))
            utils.execute("cp -r {}/data-gen {}/{}".format(in_dir, out_dir, config.data_gen_dir_name))
            os.mkdir(out_dir + "/" + config.input_dir_name)
            os.mkdir(out_dir + "/" + config.output_dir_name)
            for f in os.listdir("./temp/data"):
                if f.endswith("in"):
                    utils.execute("cp ./temp/data/{0} {1}/{2}/{0}".format(f, out_dir, config.input_dir_name))
                if f.endswith("out"):
                    utils.execute("cp ./temp/data/{0} {1}/{2}/{0}".format(f, out_dir, config.output_dir_name))
    else:
        exit(-1)
