from scapy.all import IP, TCP, UDP, ICMP
ALLOWED_PROTOCOLS = []
BLOCKED_IPS = []
ALLOWED_PORTS = []


def should_process(packet):
    """
    Returns True  → this packet should be displayed
    Returns False → skip this packet
    """
    if IP not in packet:
        return False

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    if BLOCKED_IPS:
        if src_ip in BLOCKED_IPS or dst_ip in BLOCKED_IPS:
            return False

    if ALLOWED_PROTOCOLS:
        if _get_protocol(packet) not in ALLOWED_PROTOCOLS:
            return False

    if ALLOWED_PORTS:
        src_port, dst_port = _get_ports(packet)
        if src_port not in ALLOWED_PORTS and dst_port not in ALLOWED_PORTS:
            return False

    return True


def _get_protocol(packet):
    if TCP in packet:
        return "TCP"
    elif UDP in packet:
        return "UDP"
    elif ICMP in packet:
        return "ICMP"
    return "OTHER"


def _get_ports(packet):
    """Returns (src_port, dst_port) tuple."""
    if TCP in packet:
        return packet[TCP].sport, packet[TCP].dport
    elif UDP in packet:
        return packet[UDP].sport, packet[UDP].dport
    return None, None
