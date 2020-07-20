import argparse
import server


def check_positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


parser = argparse.ArgumentParser()
# parser = argparse.ArgumentParser(prog='URL Rate Limiter')
parser.add_argument('threshold', type=check_positive_int,
                    help='Max number of requests per URL within a pre-defined time period')
parser.add_argument('ttl', type=check_positive_int,
                    help='The time period in which URL visits will be counted (in seconds)')

args = parser.parse_args()
print(args)

server.start(args.threshold, args.ttl)
