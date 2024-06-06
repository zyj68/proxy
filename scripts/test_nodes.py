import json
import time
import requests

def test_node(node):
    ip = node['ip']
    port = node['port']
    url = f"http://{ip}:{port}"
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        latency = time.time() - start
        status = response.status_code
    except requests.RequestException:
        latency = None
        status = None
    return {'ip': ip, 'port': port, 'latency': latency, 'status': status}

if __name__ == '__main__':
    with open('../data/organized_nodes.json', 'r') as file:
        nodes = json.load(file)
    results = [test_node(node) for node in nodes]
    os.makedirs('../results', exist_ok=True)
    with open('../results/test_results.json', 'w') as file:
        json.dump(results, file, indent=4)
