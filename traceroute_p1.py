from scapy.all import *
import time

def traceroute(destination, max_hops=30):
    print(f"Traceroute to {destination} with a max of {max_hops} hops:")
    for ttl in range(1, max_hops + 1):
        # Create an IP packet with the specified TTL and destination
        ip_packet = IP(dst=destination, ttl=ttl)

        # Create an ICMP echo request packet
        icmp_packet = ICMP()

        # Send the packet and wait for a response
        reply = sr1(ip_packet / icmp_packet, timeout=1, verbose=0)

        # Print the current hop
        print(f"{ttl}\t", end="")

        if reply is None:
            # No response, print '*'
            print("*")
        elif reply.type == 0:
            # ICMP Echo Reply, destination reached
            print(f"{reply.src} (Destination reached)")
            break
        elif reply.type == 11:
            # ICMP Time Exceeded, intermediate router
            print(reply.src)
        else:
            print("Unknown response")

# Usage example:
destination_ip = input("Enter the destination IP address: ")
traceroute(destination_ip)
