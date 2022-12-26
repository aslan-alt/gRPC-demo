### 安装grpcio-tools
```
pip install grpcio-tools --trusted-host mirrors.aliyun.com
```
### 编译.proto文件
```
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. itcast.proto
```
- -I表示搜索proto文件中被导入文件的目录（找依赖的目录） 
- --python_out 用于指定除service之外的所有内容，编译后文件所输出的路径（出口）
- --grpc_python_out用于指定service编译后文件所输出的路径

