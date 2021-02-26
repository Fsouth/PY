from socket import *
import getpass

# v1.1
"""         客户端          """
# *客户端配置文件

host_name = gethostname()  # 与服务器连接填服务器公网ip /本机连接获取name,  gethostname()
port_num = 1201
computer_name = gethostname()
user_name = getpass.getuser()
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host_name, port_num))
user_message = computer_name + "\t用户名: " + user_name + "\n"
clientSocket.send(user_message.encode())  # 发送客户端主机名和用户名
while True:
    message = input("input something:")
    if message == "quit":
        clientSocket.send(message.encode())  # 就算要退出,也要先告诉服务器
        clientSocket.close()
        print("****退出****")
        break
    if message == "":
        print("|~请输入有效内容~|")
        continue
    try:
        clientSocket.send(message.encode())  # 向服务端发送数据
        upMessage = clientSocket.recv(1024).decode()  # 从服务端接收数据
        print("Form the server: ", upMessage)
    except:
        # clientSocket.close()
        print("**异常退出**")
        break
