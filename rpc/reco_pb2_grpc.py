# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

# 客户端独立运行的导包方式：
# import reco_pb2 as reco__pb2

# 结合项目运行的flask-grpc客户端导包方式
from rpc import reco_pb2 as reco__pb2



class UserArticleRecommendStub(object):
  """需求：web后端需要调用推荐系统中的方法，获取推荐文章数据
  使用：user_recommend(UserRequest()) ====> 返回ArticleResponse  ====> 推荐文章数据

  定义服务---类似于python中的类
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.

      UserArticleRecommendStub().user_recommend()
    """
    self.user_recommend = channel.unary_unary(
        '/UserArticleRecommend/user_recommend',
        request_serializer=reco__pb2.UserRequest.SerializeToString,
        response_deserializer=reco__pb2.ArticleResponse.FromString,
        )


class UserArticleRecommendServicer(object):
  """需求：web后端需要调用推荐系统中的方法，获取推荐文章数据
  使用：user_recommend(UserRequest()) ====> 返回ArticleResponse  ====> 推荐文章数据

  定义服务---类似于python中的类
  """

  def user_recommend(self, request, context):
    """定义具体推荐的函数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserArticleRecommendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'user_recommend': grpc.unary_unary_rpc_method_handler(
          servicer.user_recommend,
          request_deserializer=reco__pb2.UserRequest.FromString,
          response_serializer=reco__pb2.ArticleResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'UserArticleRecommend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))