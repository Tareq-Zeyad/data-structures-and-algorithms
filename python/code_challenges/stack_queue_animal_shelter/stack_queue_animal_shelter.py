from stack_queue_animal_shelter.stack_and_queue import Queue


class AnimalShelter:
    """
    Class that holds cat/dogs attribute as FIFO >> queue
    """

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue_animal(self, animal):
        if animal.lower().startswith("cat"):
            self.cat.enqueue(animal)
        elif animal.lower().startswith("dog"):
            self.dog.enqueue(animal)
        else:
            raise Exception('Only cats/dogs are allowed')

    def dequeue_animal(self, pref):
        if pref.lower().startswith("cat"):
            return self.cat.dequeue()
        elif pref.lower().startswith("dog"):
            return self.dog.dequeue()
        else:
            return "null"
