"""A demo for parsing pcap and labelling the extracted flows.

    python3.7 examples/pparser/pparser_demo.py
"""
# Authors: kun.bj@outlook.com
#
# License: xxx
import os

from odet.pparser.parser import PCAP
from odet.utils.tool import dump

RANDOM_STATE = 42


def main():
    pcap_file = 'data/netflix.pcap'
    pp = PCAP(pcap_file, flow_pkts_thres=2, verbose=10, random_state=RANDOM_STATE)

    # extract flows from pcap
    pp.pcap2flows()
    # print(pp.features)

    # # label each flow with a label
    # label_file = 'data/demo.csv'
    # pp.label_flows(label_file=label_file)
    #
    # # flows to subflows
    # pp.flows2subflows(q_interval=0.9)

    # extract features from each flow given feat_type
    # feat_type in ['IAT', 'SIZE', 'STATS', 'SAMP_NUM', 'SAMP_SIZE']
    feat_type = 'IAT'
    print(f'feat_type: {feat_type}')
    pp.flow2features(feat_type, fft=False, header=False)
    print(pp.features.shape)

    # # dump data to disk
    # X, y = pp.features, pp.labels
    # out_dir = os.path.join('out', os.path.dirname(pcap_file))
    # dump((X, y), out_file=f'{out_dir}/demo_{feat_type}.dat')
    #
    # print(pp.features.shape, pp.pcap2flows.tot_time, pp.flows2subflows.tot_time, pp.flow2features.tot_time)


if __name__ == '__main__':
    main()
