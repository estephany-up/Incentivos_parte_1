import random
from random import randint
from string import digits, ascii_lowercase
import logging

logger = logging.getLogger(__name__)

# slices a list into n parts  of an equal size (if possible)
def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]

class CountZeroes:
    path_to_render = 'incentivos/count.html'
    name = 'Count 0s in the matrix of digits'
    def get_correct_answer(self):
        return self.data.count(str(self.value_to_count))

    def get_body(self, **kwargs):
        num_rows = kwargs.get('num_rows', 5)
        num_columns = kwargs.get('num_columns', 20)
        selection_set = kwargs.get('selection_set', [0, 1])
        self.value_to_count = kwargs.get('value_to_count', 0)
        nxm = num_rows * num_columns
        self.data = [str(random.choice(selection_set)) for _ in range(nxm)]
        self.mat = chunkify(self.data, num_rows)
        return {'mat': self.mat}

    def get_context_for_body(self):
        return {
            "mat": self.mat,
            "value_to_count": self.value_to_count,
        }