# how_to_get_mac_addresses_for_cisco_devices
How to get mac addresses of the "show mac address-table vlan &lt;vlan-id>" table with the vendor information

See sample output which is going to be parsed: 

show mac address-table vlan 100

  Vlan    Mac Address       Type        Ports
  
  ----    -----------       --------    -----
  
   100    0030.8810.105c    DYNAMIC     Gi0/3
   
   100    0008.2523.1761    DYNAMIC     Gi0/2
   
   100    e443.4b9e.03b0    DYNAMIC     Gi1/3
   
   100    00bc.6079.24d9    DYNAMIC     Gi1/2
   100    7e02.eee8.0291    DYNAMIC     Gi0/1
   100    b689.d44e.afd1    DYNAMIC     Gi1/0
   100    d207.6258.5966    DYNAMIC     Gi1/1
  Total Mac Addresses for this criterion: 7
