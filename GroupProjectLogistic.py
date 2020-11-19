import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq


def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                #print 'updated : current = %s next = %s new_dist = %s' \
                #      % (current.get_id(), next.get_id(), next.get_distance())
           # else:
                #print 'not updated : current = %s next = %s new_dist = %s' \
                 #     % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('H')
    g.add_vertex('I')
    g.add_vertex('J')
    g.add_vertex('K')
    g.add_vertex('L')
    g.add_vertex('M')
    g.add_vertex('N')

    g.add_edge('A','B',2)
    g.add_edge('B','D',2)
    g.add_edge('C','A',4)
    g.add_edge('C','F',2)
    g.add_edge('C','E',2)
    g.add_edge('D','B',2)
    g.add_edge('D','G',3)
    g.add_edge('D','H',6)
    g.add_edge('E','C',2)
    g.add_edge('E','K',4)
    g.add_edge('F','G',6)
    g.add_edge('F','C',2)
    g.add_edge('F','E',4)
    g.add_edge('F','J',2)
    g.add_edge('G','I',3)
    g.add_edge('G','F',6)
    g.add_edge('H','I',2)
    g.add_edge('H','D',6)
    g.add_edge('I','G',3)
    g.add_edge('I','J',6)
    g.add_edge('J','I',6)
    g.add_edge('J','L',5)
    g.add_edge('J','M',3)
    g.add_edge('K','M',3)
    g.add_edge('L','H',3)
    g.add_edge('L','N',4)
    g.add_edge('L','J',5)
    g.add_edge('M','J',3)
    g.add_edge('M','K',3)
    g.add_edge('N','L',4)
    g.add_edge('N','M',2)



    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex('A'), g.get_vertex('N'))

    target = g.get_vertex('N')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' % (path[::-1])
