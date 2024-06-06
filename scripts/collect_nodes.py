import requests
from bs4 import BeautifulSoup
import json
import yaml
import os

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def collect_nodes(url, selector):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    nodes = []
    for node in soup.select(selector):
        ip = node.find(class_='ip').text
        port = node.find(class_='port').text
        if ip and port:
            nodes.append({'ip': ip, 'port': port})
    return nodes

if __name__ == '__main__':
    config = load_config('../config/config.yaml')
    all_nodes = []
    for source in config['sources']:
        nodes = collect_nodes(source['url'], source['selector'])
        all_nodes.extend(nodes)
    os.makedirs('../data', exist_ok=True)
    with open('../data/nodes.json', 'w') as file:
        json.dump(all_nodes, file, indent=4)
