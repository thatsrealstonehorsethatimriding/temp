import pyshark
from views import capture_traffic

def capture_traffic(interface, display_filter, packet_count):
    capture = pyshark.LiveCapture(interface=interface, display_filter='udp')
    for packet in capture.sniff_continuously(packet_count=packet_count):
    
        print(packet)
