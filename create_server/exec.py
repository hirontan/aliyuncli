# -*- coding: utf8 -*-
#!/usr/bin/env python

import json
import argparse
from retry import retry
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest

def acs_client(api_key, api_access_key):
  return AcsClient(
    api_key,
    api_access_key,
    region_id
  );

@retry(tries=4, delay=5, backoff=2)
def request_cli(req):
  status, headers, body = clt.implementation_of_do_action(req)
  print('[ status: ' + str(status) + ' ] [ headers: ' + str(headers) + ' ] [ body: ' + str(body) + ' ]')
  if status != 200:
    raise('[ status: ' + str(status) + ' ] [ headers: ' + str(headers) + ' ] [ body: ' + str(body) + ' ]')
  json_body = json.loads(body)
  return status, json_body

def create_instance():
  req = CreateInstanceRequest.CreateInstanceRequest()
  req.set_accept_format('json')
  req.add_query_param('RegionId', region_id)
  req.add_query_param('ImageId', image_id)
  req.add_query_param('InstanceType', 'ecs.t5-lc2m1.nano')
  req.add_query_param('SecurityGroupId', '[security_group_id]')
  req.add_query_param('InstanceName', '[instance_name]')
  req.add_query_param('InternetMaxBandwidthIn', '50')
  req.add_query_param('InternetMaxBandwidthOut', '50')
  req.add_query_param('VSwitchId', '[vswitch_id]')
  req.add_query_param('SystemDisk.Size', '20')
  req.add_query_param('KeyPairName', '[key_pair_name]')
  status, body = request_cli(req)

def main():
  init_logger()
  create_instance()

def init_args():
  parser = argparse.ArgumentParser(
             prog='aliyun_sample',
             usage='python aliyun_sample.py --region [ap-northeast-1] --key [api key] --access [api access key] --image [image id],
             description='description',
             epilog='end',
             add_help=True
           )
  parser.add_argument("-r", "--region", help="please set region id", type=str, default='ap-northeast-1')
  parser.add_argument("-k", "--key", help="please set api key", type=str, required=True)
  parser.add_argument("-a", "--access", help="please set api access key", type=str, required=True)
  parser.add_argument("-i", "--image", help="please set image id", type=str, required=True)
  return parser.parse_args()

if __name__ == '__main__':
  args = init_args()
  region_id = args.region
  image_id = args.image
  clt = acs_client(args.key, args.access)
  main()
