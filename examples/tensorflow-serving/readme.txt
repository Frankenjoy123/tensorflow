��д����ͼƬ��ʶ�����ӣ�����ͼƬΪ�ڰ�ͼƬ��examplex.bmp
������ĿĿ¼��/root/tensorflow-serving
����Tensorflow serving����

docker run -it  -p 9000:9000 -v /root/tensorflow-serving/mnist-model:/model  mycat/tensorflowserving  /model_servers/tensorflow_model_server --port=9000 --model_name=mnist --model_base_path=/model

mymnist_client.py���ļ�Ϊmnist�Ŀͻ��ˣ����ӵ�tensorflow serving��ַ��Ϣ��Դ����
���з�ʽ
��������
docker run -it -v /root/tensorflow-serving/mnist-client:/ts mycat/tensorflowclient bash
cd /ts
python mymnist_client.py
���ͼƬexample3.bmp��ʶ����