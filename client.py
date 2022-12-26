import random

import grpc

import itcast_pb2
import itcast_pb2_grpc


def invoke_calculate(stub):
    work = itcast_pb2.Work()
    work.num1 = 100
    work.num2 = 200
    work.op = itcast_pb2.Work.ADD
    result = stub.Calculate(work)
    print('ADD--------')
    print(result.val)
    work.op = itcast_pb2.Work.SUBTRACT
    result = stub.Calculate(work)
    print('SUBTRACT--------')
    print(result.val)
    work.op = itcast_pb2.Work.DIVIDE
    result = stub.Calculate(work)
    print('DIVIDE--------')
    print(result.val)
    work.num2 = 0

    try:
        print('DIVIDE--------')
        result = stub.Calculate(work)
        print(result.val)
    except grpc.RpcError as e:
        print('{}:{}'.format(e.code(), e.details()))


def invoke_get_subjects(stub):
    city = itcast_pb2.City(name='bejing')
    subjects = stub.GetSubjects(city)
    for subject in subjects:
        print(subject.name)


def generate_delta():
    for _ in range(10):
        yield itcast_pb2.Delta(val=random.randint(1, 100))


def invoke_accumulate(stub):
    delta_iterator = generate_delta()
    sum = stub.Accumulate(delta_iterator)
    print('sum={}'.format(sum.val))


def generate_number():
    for _ in range(10):
        yield itcast_pb2.Delta(val=random.randint(1, 20))


def invoke_guess_number(stub):
    answers = stub.GuessNumber(generate_number())
    for answer in answers:
        print('value:{}'.format(answer.val))
        print('desc:{}'.format(answer.desc))


def run():
    with grpc.insecure_channel('127.0.0.1:8000') as channel:
        # 创建辅助客户端调用的stub对象
        stub = itcast_pb2_grpc.DemoStub(channel)
        # invoke_calculate(stub)
        # invoke_get_subjects(stub)
        # invoke_accumulate(stub)
        invoke_guess_number(stub)


if __name__ == '__main__':
    run()
