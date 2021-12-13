from GraphType import *
from QueType import *


def breadth_first_search(graph, startVertex, endVertex):
    queue = QueType()
    vertexQ = QueType()
    found = False
    print(startVertex)
    graph.get_to_vertices(startVertex, vertexQ)
    while not vertexQ.is_empty() and not found:
        item = vertexQ.dequeue()
        if item == endVertex:
            print(item)
            found = True
            return found
        else:
            queue.enqueue(item)
    while not queue.is_empty():
        item = queue.dequeue()
        print(item)
        graph.get_to_vertices(item, vertexQ)
        while not vertexQ.is_empty() and not found:
            item = vertexQ.dequeue()
            if item == endVertex:
                print(item)
                found = True
                return found
            else:
                queue.enqueue(item)
    return found

