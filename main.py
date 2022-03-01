import sipfullproxy

if __name__ == "__main__":
    hostname = sipfullproxy.socket.gethostname()
    ipaddress = sipfullproxy.socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sipfullproxy.sys.argv[1]
    print(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, 5060)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, 5060)
    server = sipfullproxy.socketserver.UDPServer(('0.0.0.0', 5060), sipfullproxy.UDPHandler)
    server.serve_forever()