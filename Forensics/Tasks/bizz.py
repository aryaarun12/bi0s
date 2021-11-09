from scapy.all import *
pt= rdpcap ( 'bizz.pcap' )
data= ''
s=''
l=len(pt)
arr=[]
for i in pt:
	data=''
	if(i.haslayer(ICMP) and i[IP].src=='10.30.8.102'):
		for j in i:
			data=data+str(j)
		s=s+data[142:]
with  open ( 'bizz.zip' , 'wb' ) as f:
	#s=hex(s)
	#d=bytes.fromhex(s)
	#s=bytes(s,'utf-8')
	f.write(s.decode("hex"))	

