from scapy.all import *
import binascii
import codecs
pkt=rdpcap("dnscap.pcap")
for c in range(1,11):
	i=1;r=[];o='';
	for p in pkt:
		if (p.haslayer(DNSQR) and not p.haslayer(DNSRR) and p[IP].src=='192.168.43.91'):
			n=p.qd.qname
			b1=n.replace(b'skullseclabs.org',b'')
			b1 = b1.replace(b'.','')
			b1=codecs.decode(b1,'hex')
			b1=b1[c:]
			if(b1 not in r):
				o=o+b1
				print(i);print(b1);print('\n')
				i+=1
				r.append(b1)        	
	with open('%d.png'%c,'wb')as f:
		f.write(o)
	f.close()
