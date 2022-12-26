import time

import itcast_pb2_grpc
import itcast_pb2
import grpc
from concurrent import futures


# 实现被调用的方法的具体代码
class DemoServer(itcast_pb2_grpc.DemoServicer):

    def Calculate(self, request, context):
        if request.op == itcast_pb2.Work.ADD:
            return itcast_pb2.Result(val=request.num1 + request.num2)
        elif request.op == itcast_pb2.Work.SUBTRACT:
            return itcast_pb2.Result(val=request.num1 - request.num2)
        elif request.op == itcast_pb2.Work.MULTIPLY:
            return itcast_pb2.Result(val=request.num1 * request.num2)
        elif request.op == itcast_pb2.Work.DIVIDE:
            if request.num2 == 0:
                # 通过设置响应状态码和描述字符串，来达到抛出异常的目的
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('cannot divide by zero')
                return itcast_pb2.Result()
            return itcast_pb2.Result(val=request.num1 // request.num2)
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('cannot divide by zero')
            return itcast_pb2.Result()


# 开启服务器，对外提供rpc调用
def server():
    # 创建服务器对象
    server_obj = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册实现的服务方法到服务器对象中
    itcast_pb2_grpc.add_DemoServicer_to_server(DemoServer(), server_obj)
    # 为服务器设置地址
    server.add_insecure_port('127.0.0.1:8000')
    # 开启服务器
    print('服务器已开启')
    server_obj.start()
    # 关闭服务器
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server_obj.stop()



if __name__ == '__main__':
    server()
