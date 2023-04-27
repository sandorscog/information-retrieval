import sys
import resource
import argparse
import time

from stream_reader import load_data
from final_operations import merge_index
#from data import load_data

# To change:
#PATH = 'C:/Users/Desktop/Desktop/Misc/UFMG/Isolada/23_1/RI'

#DATA_PATH = '/home/vboxuser/TP1/information-retrieval/corpus.jsonl'
#DATA_PATH = '/home/vboxuser/TP1/information-retrieval/slice.jsonl'

# - # - # - # - # - # - # - # - # - #

MEGABYTE = 1024 * 1024


def memory_limit(value):
    limit = value * MEGABYTE
    resource.setrlimit(resource.RLIMIT_AS, (limit, limit))


def main(data_path, index_path):
    """
    Your main calls should be added here
    """
    
    start_time = time.time()
    
    #print(corpus_path)
    load_data(data_path)
    size, num_of_keys, avg_list_size = merge_index(index_path)

    end_time = time.time()
    elapse = end_time - start_time

    final_print = f'''
{{"Index Size": {size},
"Elapsed Time": {elapse}
"Number of Lists": {num_of_keys}
"Average List Size": {avg_list_size}  }}
'''

    print(final_print)

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        '-m',
        dest='memory_limit',
        action='store',
        required=True,
        type=int,
        help='memory available'
    )

    # Other command line arguments
    parser.add_argument('-c', type=str, dest='corpus_path', action='store')
    parser.add_argument('-i', type=str, dest='final_index_path', action='store')

    # - # - # - # - # - # - # - # - # - #

    args = parser.parse_args()
    memory_limit(args.memory_limit)
    #memory_limit(1024)
    #memory_limit(4096)

    ###
    corpus_path = args.corpus_path
    #print(corpus_path)
    final_index_path = args.final_index_path
    #print(final_index_path)


    ###
    try:
        main(corpus_path, final_index_path)
        #main(corpus_path, '')
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)


# You CAN (and MUST) FREELY EDIT this file (add libraries, arguments, functions and calls) to implement your indexer
# However, you should respect the memory limitation mechanism and guarantee
# it works correctly with your implementation
