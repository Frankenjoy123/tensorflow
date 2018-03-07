import json
import argparse

# parser
parser = argparse.ArgumentParser('Generate TF_CONFIG')

parser.add_argument('task_type', type=str, help='master, ps or worker')
parser.add_argument('task_index', type=int, help='should be a valid integer')

args = parser.parse_args()

# set up de the environment
cluster = {'master': ['tf-worker-1:2222'],
           'ps': ['tf-ps-1:2222 '],
           'worker': ['tf-worker-2:2222']}

TF_CONFIG = json.dumps(
  {'cluster': cluster,
   'task': {'type': args.task_type, 'index': args.task_index},
   'model_dir': '/tensorflow/model',
   'environment': 'cloud'
  })


print(TF_CONFIG)
