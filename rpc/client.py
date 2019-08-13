# 需求：连接grpc服务器，通过stub助手调用user_recommend方法获取推荐的文章数据
import time

import grpc
import reco_pb2_grpc
import reco_pb2


def feed_articles(stub):
    """
    通过stub助手调用user_recommend方法获取推荐的文章数据
    :param stub:
    :return:
    """
    # 构建请求参数
    user_request = reco_pb2.UserRequest()
    user_request.user_id = "1"
    user_request.channel_id = 1
    user_request.article_num = 10
    user_request.time_stamp = round(time.time() * 1000)

    # 调用服务器中推荐文章的方法获取推荐文章数据
    article_response = stub.user_recommend(user_request)

    print(article_response)

    return article_response


def client():
    """
    grpc独立运行的客户端
    :return:
    """

    # 1.连接server服务器端
    with grpc.insecure_channel("127.0.0.1:8888") as channel:
        # 2.根据频道的连接信息，获取助手对象
        stub = reco_pb2_grpc.UserArticleRecommendStub(channel)
        # 文章响应结果 = stub.user_recommend(请求参数)

        # 3.通过助手对象调用推荐具体实现方法
        article_response = feed_articles(stub)


if __name__ == '__main__':
    client()