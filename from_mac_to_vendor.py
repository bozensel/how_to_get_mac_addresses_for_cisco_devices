from ttp import ttp
import urllib.request as urllib2
import json
import codecs
from netmiko import ConnectHandler

cisco = {
        'device_type' : 'cisco_ios',
        'host' : '192.168.X.Y',
        'username' : 'foo',
        'password' : '123',
}

net_connect = ConnectHandler(**cisco)
net_connect.find_prompt()
data_to_parse = net_connect.send_command("show mac address-table vlan 100")

ttp_template = '''
 {{vlan_id}}    {{mac_address}}    {{type}}     {{ports}}
'''

def mac_address_parser(data_to_parse): 
    
    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    #print(results)

    #converting str to json. 
    result = json.loads(results)

    return(result)

parsed_mac_address_parser = mac_address_parser(data_to_parse)

def find_macaddresses_vendor(mac): # REST API is used. 
    #API base url,you can also use https if you need
    url = "API URL" # Needs to be edited depending on which API server used for querying MAC Vendor. 
    #Mac address to lookup vendor from
    mac_address = mac

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

    if "company" in obj['result']:
        vendor_and_mac = str(obj['result']['company']) + "***" + str(mac_address)
        vendor_and_mac2 = vendor_and_mac.split("***")
        MAC_ADDRESSES_OUI_RESULT.append(vendor_and_mac2)
        #print(MAC_ADDRESSES_OUI_RESULT)
        #print(f"{obj['result']['company']} --> {str(mac_address)}")
        return(MAC_ADDRESSES_OUI_RESULT[0][0])
    else:
        vendor_and_mac = "NotFound" + "***" + str(mac_address)
        vendor_and_mac2 = vendor_and_mac.split("***")
        MAC_ADDRESSES_OUI_RESULT.append(vendor_and_mac2)
        #print(MAC_ADDRESSES_OUI_RESULT)
        return(MAC_ADDRESSES_OUI_RESULT[0][0])
        #print(f"Not Found --> {str(mac_address)}")

for mac_address in parsed_mac_address_parser[0]:
    mac = mac_address['mac_address'][:7]
    mac2 = mac.split(".")
    mac3 = f"{mac2[0][:2]}:{mac2[0][2:]}:{mac2[1]}"
    print(f"Vlan ID: {mac_address['vlan_id']} Mac Address: {mac_address['mac_address']} --> Vendor: {find_macaddresses_vendor(mac3)}")
