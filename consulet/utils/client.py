import grpc

from auth_pb2 import tokeninput
from auth_pb2_grpc import TokenValidationStub


channel = grpc.insecure_channel('127.0.0.1:50051')
client = TokenValidationStub(channel)
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMzA5Mzc0MiwianRpIjoiY2RjZTEwZDMtNTkxNi00YTBkLTk5ODYtZTUwNWJhNmE1ZWE2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFtaXJAZ21haWwuY29tIiwibmJmIjoxNjMzMDkzNzQyLCJleHAiOjE2MzgyNzc3NDJ9.pD3yqhGUohXJ0zxjUOF6ETGyllrTDW3XInMObmI1tVc"
# send Phone Number to varify it is the same in db
request = tokeninput(token=token)
req = client.validate(request)
print(req.email)
