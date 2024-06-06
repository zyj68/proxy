import json

def organize_nodes(input_file, output_file):
    with open(input_file, 'r') as file:
        nodes = json.load(file)
    organized_nodes = sorted(nodes, key=lambda x: x['ip'])
    with open(output_file, 'w') as file:
        json.dump(organized_nodes, file, indent=4)

if __name__ == '__main__':
    organize_nodes('../data/nodes.json', '../data/organized_nodes.json')
