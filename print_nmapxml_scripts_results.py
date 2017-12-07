# Needs python-libnmap
import sys
from libnmap.parser import NmapParser

def usage(script_name):
    print "Nmap XML Script Results Parser"
    print
    print "Usage: %s report_file.xml"
    
def main():
    if not len(sys.argv[1:]):
        usage(sys.argv[0])
        sys.exit(0)
        
    parser = NmapParser.parse_fromfile(sys.argv[1])
    for host in parser.hosts:
        print host.id
        for results in host.scripts_results:
            print "  %s" % results['id']
            if not results['elements']:
                print "    %s" % results['output']
                print
                continue
            for element in results['elements']:
                print "    %s" % element
                for k,v in results['elements'][element].iteritems():
                    print "    %s : %s" % (k, v.rstrip())
                
                print
                
if __name__ == '__main__':
    main()
    sys.exit(0)