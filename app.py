from flask import Flask, jsonify
import os

app = Flask(__name__)

# Downward API를 통해 전달된 환경 변수에서 Pod의 이름, 노드 이름, 네임스페이스를 가져옴.
@app.route('/') # 루트 디렉토리에 접근시에 호출되는 메소드
def pod_info():
    pod_name = os.getenv('POD_NAME', 'Unknown')
    node_name = os.getenv('NODE_NAME', 'Unknown')
    pod_namespace = os.getenv('POD_NAMESPACE', 'Unknown')
    
    return jsonify({
        'pod_name': pod_name,
        'node_name': node_name,
        'pod_namespace': pod_namespace
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) # 모든 네트워크 인터페이스에서 접근 가능하게 하고, 8080 포트에서 서버 실행
