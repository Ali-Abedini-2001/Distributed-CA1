import grpc
import time
from protos1 import order_management_python_pb2
from protos1 import order_management_python_pb2_grpc


def get_client_stream_requests():
    while True:
        item = input("Please enter an item (or nothing to stop): ")

        if item == "":
            break

        order_request = order_management_python_pb2.OrderRequest(item = item)
        yield order_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_management_python_pb2_grpc.OrderManagementStub(channel)
        print("1. Unary")
        print("2. Server Side Streaming")
        print("3. Client Side Streaming")
        print("4. Both Streaming")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            order_request = order_management_python_pb2.OrderRequest(item = "apple")
            order_response = stub.GetUnaryOrder(order_request)
            print("Unary Mode:")
            print(order_response)
        elif rpc_call == "2":
            order_request = order_management_python_pb2.OrderRequest(item = "banana")
            order_responses = stub.GetSSOrder(order_request)

            for order_response in order_responses:
                print("GetSSOrder Response Received:")
                print(order_response)
        elif rpc_call == "3":
            delayed_reply = stub.GetCSOrder(get_client_stream_requests())

            print("GetCSOrder Response Received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.GetBothOrder(get_client_stream_requests())

            for response in responses:
                print("GetBothOrder Response Received: ")
                print(response)
    

if __name__ == '__main__':
    run()
