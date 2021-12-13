from GraphType import *

def depth_first_search(graph, startVertex, endVertex):
    stack = StackType()
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
            stack.push(item)
    while not stack.is_empty():
        item = stack.top()
        print(item)
        stack.pop()
        graph.get_to_vertices(item, vertexQ)
        while not vertexQ.is_empty() and not found:
            item = vertexQ.dequeue()
            if item == endVertex:
                print(item)
                found = True
                return found
            else:
                stack.push(item)
    return found
