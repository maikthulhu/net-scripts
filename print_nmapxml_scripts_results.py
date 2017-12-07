# Needs python-libnmap
import sys
import argparse

from libnmap.parser import NmapParser

def main():
    argp = argparse.ArgumentParser(description='''
Nmap XML Script Results Parser
by: maik''',
                                   formatter_class=argparse.RawTextHelpFormatter)
    argp.add_argument('report_file', help='XML-formatted Nmap output')
    argp.add_argument('-b', '--brief', action='store_true', help='Brief output')
    args = argp.parse_args()

    parser = NmapParser.parse_fromfile(args.report_file)
    for host in parser.hosts:
        print host.id
        for results in host.scripts_results:
            if not results['elements'] and args.brief:
                continue
            elif not results['elements'] and not args.brief:
                print "  {}".format(results['id'])
                print "    {}".format(results['output'])
                print
                continue
            else:
                print "  {}".format(results['id'])

            for element in results['elements']:
                if not args.brief:
                    print "    {}".format(element)
                for k,v in results['elements'][element].iteritems():
                    if args.brief:
                        if k == 'state':
                            print "    {} : {}".format(k, v.rstrip())
                            break
                        else:
                            continue
                    print "    {} : {}".format(k, v.rstrip())
                
                print
                
if __name__ == '__main__':
    main()
    sys.exit(0)
