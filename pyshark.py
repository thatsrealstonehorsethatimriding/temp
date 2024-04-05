import pyshark

def capture_traffic(interface, display_filter, packet_count):
    capture = pyshark.LiveCapture(interface=interface, display_filter=display_filter)
    for packet in capture.sniff_continuously(packet_count=packet_count):
        # Burada paketleri analiz edebilir ve istediğiniz işlemleri gerçekleştirebilirsiniz
        print(packet)
