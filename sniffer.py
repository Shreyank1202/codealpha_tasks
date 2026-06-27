# sniffer.py

from scapy.all import sniff
from packet_handler import process_packet
import sys


def start_sniffer(interface=None, filter_str=None, packet_count=0):
    """
    Starts the network sniffer.
    - interface:    which network card to listen on (None = auto)
    - filter_str:   BPF filter e.g. "tcp", "udp", "icmp", "port 80"
    - packet_count: how many packets to capture (0 = infinite)
    """
    print("=" * 60)
    print("         BASIC NETWORK SNIFFER")
    print("=" * 60)
    print(f"[*] Interface : {interface if interface else 'Auto-detect'}")
    print(
        f"[*] Filter    : {filter_str if filter_str else 'None (all packets)'}")
    print(f"[*] Count     : {packet_count if packet_count else 'Unlimited'}")
    print(f"[*] Press Ctrl+C to stop")
    print("-" * 60)

    try:
        sniff(
            iface=interface,       # which network interface to use
            filter=filter_str,     # BPF filter string
            prn=process_packet,    # function to call on every packet
            count=packet_count,    # 0 means capture forever
            store=False            # don't store packets in memory (saves RAM)
        )
    except PermissionError:
        print("[!] ERROR: Permission denied.")
        print("[!] Please run VS Code or terminal as Administrator.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Sniffer stopped.")
        sys.exit(0)


if __name__ == "__main__":

    INTERFACE = None    # None = auto. Or use "Wi-Fi" / "Ethernet"
    FILTER = None    # None = all. Or "tcp" / "udp" / "icmp" / "port 443"
    COUNT = 0
    # ───────────────────────────────────────────────────────

    start_sniffer(
        interface=INTERFACE,
        filter_str=FILTER,
        packet_count=COUNT
    )
