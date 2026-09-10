"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like.Create the data structures to maintain this system and implement operations
such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked List data structure.
"""

from collections import deque


class AnimalShelter(object):

    def __init__(self):
        self.cat_q = deque()
        self.dog_q = deque()
        self.gl_count = 0

    def enqueue(self, animal):
        num , type = animal
        entry = (self.gl_count , num)
        self.gl_count += 1
        (self.dog_q if type == 1 else self.cat_q).append(entry)

    def dequeue_any(self):
        if not self.cat_q:
            return self._pop(self.dog_q , 1)
        if not self.dog_q:
            return self._pop(self.cat_q, 0)
        if self.cat_q[0][0] < self.dog_q[0][0]:
            return self._pop(self.cat_q, 0)
        else:
            return self._pop(self.dog_q , 1)

    def _pop(self , q , kind):
        if not q:
            return [-1 , -1]
        c, num = q.popleft()
        return [num , kind]

    def dequeue_dog(self):
        return self._pop(self.dog_q, 1)

    def dequeue_cat(self):
        return self._pop(self.cat_q, 0)