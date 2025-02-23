from scapy.all import *
import sys

def traceroute(destination, max_hops=15):
    timeout = 1  # Timeout period for each hop in seconds
    print(f"Traceroute to {destination} (max hops: {max_hops}):\n")

    for ttl in range(1, max_hops + 1):
        packet = IP(dst=destination, ttl=ttl) / ICMP()

        reply = sr1(packet, verbose=0, timeout=timeout)

        if reply is None:
            print(f"{ttl} *")
        elif reply.type == 11:  # ICMP Time Exceeded
            print(f"{ttl} {reply.src}")
        elif reply.type == 0:  # ICMP Echo Reply
            print(f"{ttl} {reply.src} (Reached destination)")
            break
    else:
        print("Max hops reached without reaching the destination.")

if __name__ == "__main__":
    destination_ip = input("Enter the destination IP address: ")
    max_hops = int(input("Enter the maximum number of hops (default 15): ") or 15)
    traceroute(destination_ip, max_hops)
