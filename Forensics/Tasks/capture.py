from scapy.all import *
packet= rdpcap ( 'capture.pcap' )
data= '' 
for p in packet:
     if p.haslayer (ICMP):
         if p [IP].src == '192.168.1.200' :
            data=data+(p [Raw] .load)
#data=str.encode(data)
with  open ( 'flag.zip' , 'wb' ) as f:
    f.write (data)
