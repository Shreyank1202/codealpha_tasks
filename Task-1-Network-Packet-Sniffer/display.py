import datetime
import os

LOG_FILE = "logs/packets.log"


def display_packet(packet_info):
    """
    Formats and prints packet info to the terminal.
    Also saves to log file.
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    src = packet_info["src_ip"]
    dst = packet_info["dst_ip"]

    if packet_info["src_port"]:
        src = f"{src}:{packet_info['src_port']}"

    if packet_info["dst_port"]:
        dst = f"{dst}:{packet_info['dst_port']}"
    lines = [
        f"\n[Packet #{packet_info['count']}]  {timestamp}  |  {packet_info['size']} bytes",
        f"  Protocol : {packet_info['protocol']}",
        f"  Source   : {src}",
        f"  Dest     : {dst}",
        f"  Payload  : {packet_info['payload']}",
        "-" * 60
    ]

    for line in lines:
        print(line)
    log_to_file(lines)


def log_to_file(lines):
    """
    Appends packet info to logs/packets.log
    Creates the logs/ folder if it doesn't exist yet.
    """
    try:
        os.makedirs("logs", exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    except Exception as e:
        print(f"[!] Logging error: {e}")
