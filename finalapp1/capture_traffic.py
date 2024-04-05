from django.http import HttpResponse
from django.shortcuts import render
import pyshark

def capture_traffic(request):
    # Ağ dinleme işlevini çağırın
    capture_traffic(interface='eth0', display_filter='udp', packet_count=10)
    return HttpResponse("Ağ trafiği dinleniyor...")