## rpc and dbp sync data

### 仅同步区块数据
```bash
sudo pip3 install requests
sudo pip3 install json
sudo pip3 install pymysql
./task.py
```

### 同步交易池数据和区块数据
```bash
sudo pip3 install requests
sudo pip3 install json
sudo pip3 install pymysql
sudo pip3 install protobuf
protoc ./dbp/dbp.proto  --python_out=./
protoc ./dbp/lws.proto  --python_out=./
./dbp.py
```