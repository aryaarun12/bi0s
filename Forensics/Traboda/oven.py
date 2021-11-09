from scapy.all import *
packet= rdpcap ( '../oven.pcapng' )
for p in packet:
#     if (p.haslayer(UDP) and len(p)==1392):
#            d = str(p[UDP].payload)
#	    dd=dd+d
	if (p.haslayer(TCP) and len(p)==854):
		if(p.dport==444):
			d1=d1+str(p[TCP].payload)
		if(p.dport==81):
			d2=d2+str(p[TCP].payload)
with  open ( '444' , 'wb' ) as f:
	f.write(d1)
with  open ( '81' , 'wb' ) as f:
	f.write(d2)

nd1=''; nd2='';
for i in d1:
	c=chr((ord(i)-5)%256)
	nd1=nd1+c
for i in d2:
	c=chr((ord(i)-5)%256)
	nd2=nd2+c
	
with  open ( '444.pdf' , 'wb' ) as f:
	f.write(nd1)
with  open ( '81.zip' , 'wb' ) as f:
	f.write(nd2)

	



 
