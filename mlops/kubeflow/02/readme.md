## Dependencies

Python 3.8.17
- kfp==1.8.22
- kfp-pipeline-spec==0.1.16
- kfp-server-api==1.8.5
- python-dotenv==1.0.0

## How to use
1. make `.env` in your path with pipeline.py 
2. write your credentials to access kubeflow
3. run pipeline.py

```.env
# .env

HOST=http://example.com
USERNAME=user@example.com
PASSWORD=passwordexample
NAMESPACE=kubeflow-example-namespace
```