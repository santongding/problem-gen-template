# 本仓库为出ACM题的简易模版
## 新建题目
- 需要增加题目时, 可以复制problems/squares并重命名为<your_prob>
## 数据生成
- data-gen文件夹下所有文件必须保留(when all data is static, data_gen.py can be removed), 其中validator为数据格式验证, data_gen为数据生成, gen-config.csv为每组数据的参数, 使用参数的方法见模板题中的data_gen.py/validator.py, 其中第一列data_id为数据组号, 可以增加列数, 但每个数据必须为整数
- gen-config中第二列is_static表示此数据是否为静态的, 若为静态的, 需要从data-gen/input文件夹下读取相应数据. 否则动态生成
## 文档
- docs文件夹中存放题面题解等, 后续打包时此文件夹中文件会直接复制
## 标程
- std文件夹中存放标程, 且必须要有一个命名为std.cpp的文件作为标准答案输出
- 可以通过给标程程序添加 _ + 后缀 来限定此程序的时间, 例如std233_5.cpp的时限为5s(后缀只能是整数), 若不加后缀默认1s时限. 注意, std.cpp不能添加后缀
- 可以通过设置环境变量CUR_PROB=<your_prob>来更改当前工程调试的题目
- 可通过cmake build完成后, 直接运行${CUR_PROB}/std文件夹中的各个标程, 具体可查看CMakeList.txt
## 测试
- checker.py/batch-test.sh用于检查各个标程间的答案是否正确, 在使用前务必设置CUR_PROB=<your_prob>
- 当题目被修改后, 将会触发github action的自动测试
## 打包
- pack-config.txt配置了打包后各个文件夹的名称及需要打包的题目
- pack.py为打包脚本
- 当题目被更改或打包配置被更改时, 会触发自动打包程序并发布github release
