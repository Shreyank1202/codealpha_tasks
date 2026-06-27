# packet_handler.py
# Processes every packet captured by Scapy
# Extracts: Source IP, Dest IP, Protocol, Ports, Payload

from scapy.all import IP, TCP, UDP, ICMP, Raw
from display import display_packet
from filters import should_process

# Global packet counter
packet_count = 0


def process_packet(packet):
    """
    Scapy calls this function automatically for EVERY captured packet.
    We extract information from the packet and send it to display.
    """
    global packet_count

    if IP not in packet:
        return

    # Check our custom filter (defined in filters.py)
    if not should_process(packet):
        return

    packet_count += 1

    # ── EXTRACT IP LAYER INFO ──────────────────────────────
    src_ip = packet[IP].src       # Source IP address
    dst_ip = packet[IP].dst       # Destination IP address

    # ── IDENTIFY PROTOCOL ─────────────────────────────────
    protocol = get_protocol(packet)

    # ── EXTRACT PORTS (TCP and UDP only) ──────────────────
    src_port = None
    dst_port = None

    if TCP in packet:
        src_port = packet[TCP].sport   # Source port
        dst_port = packet[TCP].dport   # Destination port
    elif UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
    payload = get_payload(packet)

    packet_info = {
        "count": packet_count,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "src_port": src_port,
        "dst_port": dst_port,
        "payload": payload,
        "size": len(packet)
    }

    display_packet(packet_info)


def get_protocol(packet):
    """
    Returns a human-readable protocol name.
    Scapy checks if a layer EXISTS inside the packet using 'in'.
    """
    if TCP in packet:
        return "TCP"
    elif UDP in packet:
        return "UDP"
    elif ICMP in packet:
        return "ICMP"
    else:

        return f"OTHER (proto={packet[IP].proto})"


def get_payload(packet):
    """
    Extracts the actual data/payload from the packet.
    Raw layer = the actual application data being sent.
    We limit display to first 100 characters to keep output clean.
    """
    if Raw in packet:
        raw_data = packet[Raw].load
        try:

            return raw_data.decode("utf-8", errors="replace")[:100]
        except Exception:

            return raw_data.hex()[:100]

    return "No payload"
