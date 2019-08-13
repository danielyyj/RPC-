# RPC-
Remote Procedure Call，缩写为 RPC，也叫远程程序调用

相比于传统HTTP的实现而言：

优点
效率高
发起RPC调用的一方，在编写代码时可忽略RPC的具体实现，如同编写本地函数调用一样
缺点
通用性不如HTTP好 因为传输的数据不是HTTP协议格式，所以调用双方需要专门实现的通信库，对于不同的编程开发语言，都要有相关实现。而HTTP作为一个标准协议，大部分的语言都已有相关的实现，通用性更好。
HTTP更多的面向用户与产品服务器的通讯。

RPC更多的面向产品内部服务器间的通讯。 thrift

RPC结构
RPC的设计思想是力图使远程调用中的通讯细节对于使用者透明，调用双方无需关心网络通讯的具体实现。因而实现RPC要进行一定的封装。
