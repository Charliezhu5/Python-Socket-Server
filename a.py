import pickle
import sys

a = ('a', 'b', 'c', 'd', 'e')
p = pickle.dumps(a)

print(str(sys.getsizeof(p)).encode('utf-8'))