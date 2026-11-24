from node import Node
from algorithms.common import find_possible_moves
from time import process_time


class DFS:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.kirbyPos = self.firstNode.searchForKirby()
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()
        expandedNodes = 0
        depth = 0

        # TODO: define required variables here
        currentNode = self.firstNode
        visited = [currentNode]

        while not currentNode.isGoal():
            possible_moves = find_possible_moves(currentNode)
            next_node = None
            for move in possible_moves:
                # Don't alter this
                if move.getDepth() > depth:
                    depth = move.getDepth()

                next_node = move
                if next_node not in visited:
                    visited.append(next_node)
                    break

            # TODO: Implement your code here
            if next_node is not None:
                next_node.setFather(currentNode)
                currentNode = next_node
            elif currentNode.getOperator() != "first father":
                currentNode = currentNode.getFather()
            else:
                print("there isn't any path")
                break

            # Don't alter this
            expandedNodes += 1

        # Don't alter this
        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes + 1)  # Good
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes + 1, depth]

