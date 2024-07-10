import unittest
from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
from server.server import Greeter

class GreeterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), cls.server)
        cls.server.add_insecure_port('[::]:50051')
        cls.server.start()

        cls.channel = grpc.insecure_channel('localhost:50051')
        cls.stub = helloworld_pb2_grpc.GreeterStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        cls.channel.close()
        cls.server.stop(None)

    def test_say_hello(self):
        request = helloworld_pb2.HelloRequest(name='test')
        response = self.stub.SayHello(request)
        self.assertEqual(response.message, 'Hello, test')

if __name__ == '__main__':
    unittest.main()
