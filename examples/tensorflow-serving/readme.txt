手写输入图片的识别例子，测试图片为黑白图片，examplex.bmp
下载项目目录到/root/tensorflow-serving
启动Tensorflow serving容器

docker run -it  -p 9000:9000 -v /root/tensorflow-serving/mnist-model:/model  mycat/tensorflowserving  /model_servers/tensorflow_model_server --port=9000 --model_name=mnist --model_base_path=/model

mymnist_client.py等文件为mnist的客户端，连接的tensorflow serving地址信息在源码中
运行方式
启动容器
docker run -it -v /root/tensorflow-serving/mnist-client:/ts mycat/tensorflowclient bash
cd /ts
python mymnist_client.py
输出图片example3.bmp的识别结果