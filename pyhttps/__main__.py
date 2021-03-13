import sys
from .pyhttps import startServer,generate_selfsigned_cert

def main():
    try:
        usage="""
            USAGE:
                pysrvhttps.py [-option value] [port]
            OPTIONS:
                -p              Port Number [Port 443,80 requires sudo]
                -h              Host address
                -c              ssl cert file location
                -k              ssl key file location
                -gencert        Auto Generate SSL Cert and Key [openssl must be installed and included in PATH]
        """

        h='0.0.0.0'
        p=4443
        c=""
        k=""
        if len(sys.argv)>1:
            if "-gencert" in sys.argv:
                generate_selfsigned_cert()
            if "-p" in sys.argv:
                try:
                    p=int(sys.argv[sys.argv.index('-p')+1])
                except:
                    print("Invalid port!\n",usage)
            if "-h" in sys.argv:
                try:
                    h=sys.argv[sys.argv.index('-h')+1]
                except:
                    print("Invalid host!\n",usage)
            if "-c" in sys.argv:
                try:
                    c=sys.argv[sys.argv.index('-c')+1]
                except:
                    print("Invalid cert!\n",usage)
            if "-k" in sys.argv:
                try:
                    k=sys.argv[sys.argv.index('-k')+1]
                except:
                    print("Invalid key!\n",usage)
            if len(sys.argv)==2 and sys.argv[1]!="-gencert":
                try:
                    p=int(sys.argv[1])
                except:
                    print("Invalid port!\n",usage)
            try:
                p=int(sys.argv[-1])
            except:
                pass
        # you can change the host and port
        startServer(h,p,c,k)
    except KeyboardInterrupt:
            print("\nFile Server Stopped!")

if __name__ == "__main__":
    main()