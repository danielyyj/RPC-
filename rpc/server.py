import time
import grpc
# 在python3.2之后推出了concurrent并发模块
from concurrent.futures import ThreadPoolExecutor
import reco_pb2_grpc
import reco_pb2


class UserArticleRecommendServicer(reco_pb2_grpc.UserArticleRecommendServicer):
    """
    给用户推荐文章的服务
    """
    def user_recommend(self, request, context):
        """
        给用户推荐文章具体业务逻辑实现
        :param request: UserRequest类的请求参数对象
        :param context: 错误信息
        :return:
        """
        # 1.获取web后端的请求参数
        user_id = request.user_id
        channel_id = request.channel_id
        # 推荐文章的数量
        article_num = request.article_num
        time_stamp = request.time_stamp
        # 2.参数校验

        # 3.逻辑处理
        # TODO: 后续补充推荐系统的业务逻辑
        # 伪推荐 造数据
        # 4.返回值处理
        article_response = reco_pb2.ArticleResponse()
        # 曝光数据
        article_response.exposure = "exposure message"
        article_response.time_stamp = round(time.time() * 1000)

        article_list = []
        for i in range(article_num): # 0 1 2 3

            # 创建文章对象
            article = reco_pb2.Article()
            # 给文章id赋值
            article.article_id = i + 1
            # 用户行为埋点数据
            article.track.click = "click action {}".format(i+1)
            article.track.collect = "collect action {}".format(i+1)
            article.track.share = "share action {}".format(i+1)
            article.track.read = "read action {}".format(i+1)
            article_list.append(article)

        # extend 在列表尾部补充元素
        article_response.recommends.extend(article_list)

        return article_response


def server():
    """
    创建grpc的服务器
    :return:
    """

    # 1.创建服务器对象,以线程池的方式运行服务器，最大并发10
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=10))

    # 2.给服务器绑定ip地址和端口号
    server.add_insecure_port("127.0.0.1:8888")

    # 3.往服务器中添加服务  --- 往服务器中添加文章推荐的服务
    # 参数1：文章推荐服务对象：UserArticleRecommendServicer()
    # 参数2：服务器：server
    reco_pb2_grpc.add_UserArticleRecommendServicer_to_server(UserArticleRecommendServicer(), server)

    # 4.启动服务器
    # 注意点：默认的服务器开启是非阻塞--程序自动退出
    # 解决：作为独立运行的服务器，应该采取阻塞的方式运行，程序才不会退出
    server.start()

    # 单独运行grpc服务器
    # 阻塞让程序不自动退出
    while True:
        time.sleep(10)


if __name__ == '__main__':
    # python server.py 运行服务器
    server()