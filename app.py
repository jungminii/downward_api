from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def downwardApi():
    pod_name = os.getenv('POD_NAME', '알 수 없는 Pod')
    node_name = os.getenv('NODE_NAME', '알 수 없는 Node')
    pod_namespace = os.getenv('POD_NAMESPACE', '알 수 없는 Namespace')
    
    return f"Container EDU | POD 이름: {pod_name} | 노드 이름: {node_name} | 네임스페이스: {pod_namespace}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

