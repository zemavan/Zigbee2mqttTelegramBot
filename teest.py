import yaml
def fileopen(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
        # print(data)
        for i in data['devices']:
            print (i)
fileopen('/home/rootman/projcet_zigbee2mqttTelegBot/zigbee2mtt/zigbee2mqtt/data/configuration.yaml')