from QueType import *
from StackType import *

NULL_EDGE = 0

def index_is(vertices, vertex):
    index = 0
    while index < len(vertices) and vertex != vertices[index]:
        index += 1
    if not index < len(vertices):
        return -1
    else:
        return index

class GraphType:
    def __init__(self, maxV=50):
        self.numVertices = 0
        self.maxVertices = maxV
        self.vertices = [None] * maxV
        self.edges = [[NULL_EDGE] * maxV for _ in range(maxV)]
        self.marks = [None] * maxV

    def add_vertex(self, vertex):
        self.vertices[self.numVertices] = vertex
        self.numVertices += 1
        i = 0
        while i < self.numVertices:
            self.edges[self.numVertices][i] = NULL_EDGE
            self.edges[i][self.numVertices] = NULL_EDGE
            i += 1

    def add_edge(self, fromVertex, toVertex, weight):
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        self.edges[row][col] = weight

    def weight_is(self, fromVertex, toVertex):
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        return self.edges[row][col]

    def get_to_vertices(self, vertex, adjVertices):
        fromindex = index_is(self.vertices, vertex)
        i = 0
        while i < self.numVertices:
            if self.edges[fromindex][i] != NULL_EDGE:
                adjVertices.enqueue(self.vertices[i])
            i += 1

    def clear_marks(self):
        self.marks = [0] * maxV

    def is_marked(self, vertex):
        vertexindex = index_is(self.vertices, vertex)
        return self.marks[vertexindex] != 0

    def mark_vertex(self, vertex):
        vertexindex = index_is(self.vertices, vertex)
        self.marks[vertexindex] = 1

    def delete_edge(self, fromVertex, toVertex):
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        self.edges[row][col] = 0

