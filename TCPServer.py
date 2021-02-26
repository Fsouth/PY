from socket import *

# v1.1
"""          服务端            """
# *服务器配置文件

serverSocket = socket(AF_INET, SOCK_STREAM)
# ! 服务器要开放1201端口
serverSocket.bind((gethostname(), 1201))  # gethostname() 连接服务器则换成服务器的内网ip,字符串格式,如'192.123.2.12',本机连接不需要改动(与客户端相同)
serverSocket.listen(5)
print("-----start-----")
connectionSocket, address = serverSocket.accept()
print("连接的主机ip为:", address, "\n", "\r主机名为: ", connectionSocket.recv(1024).decode())
#!多用户连接问题 多线程处理,堵塞问题(开放多个端口?),退出问题
while True:
    print("连接的主机ip为:", address)
    print("Waitting")
    try:
        message = connectionSocket.recv(1024).decode()  # 从客户端接收数据
        if message == "quit":
            connectionSocket.close()
            print("----退出----")  # 如果出错就运行
            break
        try:
            print("The meaage from Client: ", message + "\n")
            """ 接收到数据后开始处理 """
            end_message = ("****" + message.upper() + "****").encode()  # 服务器处理数据
            connectionSocket.send(end_message)  # 向客户端发送数据
        except:
            connectionSocket.close()
            print("--异常退出--")  # 如果出错就运行
            break
    except:
        connectionSocket.close()
        print("客户端已退出,接收数据出错")
        break
