#!/usr/bin/env python3
from scapy.all import * # pyright: ignore[reportWildcardImportFromLibrary]
import sys

def packet_callback(packet):
    """Callback function for each captured packet"""
    
    if packet.haslayer(IP): # type: ignore
        ip_src = packet[IP].src # type: ignore
        ip_dst = packet[IP].dst # type: ignore
        proto = packet[IP].proto # type: ignore
        
        protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        proto_name = protocols.get(proto, str(proto))
        
        print(f"\n[+] Source: {ip_src} -> Destination: {ip_dst}")
        print(f"[+] Protocol: {proto_name}")
        
        # Check if it's HTTP (port 80)
        if packet.haslayer(TCP): # type: ignore
            if packet[TCP].sport == 80 or packet[TCP].dport == 80: # type: ignore
                if packet.haslayer(Raw):
                    payload = packet[Raw].load[:200]
                    print(f"[+] HTTP Payload: {payload}")
        
        if packet.haslayer(Raw):
            payload = packet[Raw].load[:50]
            print(f"[+] Payload (first 50 bytes): {payload}")
        
        print("-" * 50)

def main():
    print("[*] Starting Network Sniffer...")
    print("[*] Press Ctrl+C to stop")
    
    try:
        # Filter for HTTP traffic only
        sniff(filter="tcp port 80", prn=packet_callback, count=10)
    except KeyboardInterrupt:
        print("\n[*] Sniffer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
