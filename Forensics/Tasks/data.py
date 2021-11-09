from scapy.all import *
packet= rdpcap ( 'data.pcap' )
j=''
for p in packet:
     if p.haslayer (ICMP):
         if p [IP].src == '10.136.255.127' :
            tb = chr(p[ICMP].type)
	    j=j+tb
#data=str.encode(data)
with  open ( 'flag.gif' , 'wb' ) as f:
    f.write(j)
    
