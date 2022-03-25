# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


# from searchAgents import PositionSearchProblem


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


import searchAgents


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    specifiedActions = []  # list of action that I will return to get the goal
    previouslyVisited = set()  # I use it as a reference as not to visit a place twice
    problemStack = util.Stack()  # it will be easier to save the point and path to those points

    # previouslyVisited.add(problem.getStartState()) # add initial state as visited

    problemStack.push((problem.getStartState(), []))

    if problem.isGoalState(problem.getStartState()):  # I sucess before i do anything
        return []

    while not problem.isGoalState(problem.getStartState()):  # While i couldn't achieve the goal

        point, pathToPoint = problemStack.pop()
        previouslyVisited.add(point)

        if problem.isGoalState(point):
            return pathToPoint

        nextPossibleMoves = problem.getSuccessors(point)

        if nextPossibleMoves:
            nextPossibleMoves.sort(key=lambda t: t[2])  # sory them alphapitically to use the first one first
            for move in nextPossibleMoves:
                if not move[0] in previouslyVisited:
                    newPathToPoint = pathToPoint + [move[1]]
                    problemStack.push((move[0], newPathToPoint))

    # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    """
    changes over DFS
    1- previouslyVisited make it list as set hashes and i can't insert a unhashable list
    2- convert from stack to queue
    3-
    """
    "*** YOUR CODE HERE ***"
    pathToPoint = []  # list of action that I will return to get the goal
    previouslyVisited = []  # I use it as a reference as not to visit a place twice
    problemQueue = util.Queue()  # it will be easier to save the point and path to those points

    # previouslyVisited.add(problem.getStartState()) # add initial state as visited

    problemQueue.push((problem.getStartState(), []))

    if problem.isGoalState(problem.getStartState()):  # I success before I do anything
        return []

    while not problem.isGoalState(problem.getStartState()):  # While I couldn't achieve the goal

        if problemQueue.isEmpty():
            return []

        point, pathToPoint = problemQueue.pop()
        previouslyVisited.append(point)

        if problem.isGoalState(point):
            return pathToPoint

        nextPossibleMoves = problem.getSuccessors(point)

        if nextPossibleMoves:
            nextPossibleMoves.sort(key=lambda t: t[2])  # sort them alphabetically to use the first one first
            for move in nextPossibleMoves:
                if not move[0] in previouslyVisited:
                    newPathToPoint = pathToPoint + [move[1]]
                    problemQueue.push((move[0], newPathToPoint))


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first.

    should be same as UCS but only different in the cost, we just add a new term to the cost funtion
    but i assume we still use priority queue
    """

    "*** YOUR CODE HERE ***"
    problemPriorityQueue = util.PriorityQueue()
    previouslyVisited = set()  # I use it as a reference as not to visit a place twice

    problemPriorityQueue.push((problem.getStartState(), []), 1 / (problem.getStartState()[0] ** 2))

    if problem.isGoalState(problem.getStartState()):
        return []

    while not problem.isGoalState(problem.getStartState()):
        point, pathToPoint = problemPriorityQueue.pop()
        previouslyVisited.add(point)

        if problem.isGoalState(point):
            return pathToPoint

        nextPossibleMoves = problem.getSuccessors(point)

        if nextPossibleMoves:
            nextPossibleMoves.sort(key=lambda t: t[2])  # sort them alphapitically to use the first one first
            for move in nextPossibleMoves:
                if not move[0] in previouslyVisited:
                    newPathToPoint = pathToPoint + [move[1]]
                    # problemPriorityQueue.push((move[0], newPathToPoint),1/move[0][0]**2)
                    problemPriorityQueue.push((move[0], newPathToPoint), problem.getCostOfActions(newPathToPoint))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    problemPriorityQueue = util.PriorityQueue()
    previouslyVisited = set()  # I use it as a reference as not to visit a place twice

    problemPriorityQueue.push((problem.getStartState(), []), 1 / (problem.getStartState()[0] ** 2))

    if problem.isGoalState(problem.getStartState()):
        return []

    while not problem.isGoalState(problem.getStartState()):
        point, pathToPoint = problemPriorityQueue.pop()
        previouslyVisited.add(point)

        if problem.isGoalState(point):
            return pathToPoint

        nextPossibleMoves = problem.getSuccessors(point)

        if nextPossibleMoves:
            nextPossibleMoves.sort(key=lambda t: t[2])  # sort them alphapitically to use the first one first
            for move in nextPossibleMoves:
                if not move[0] in previouslyVisited:
                    newPathToPoint = pathToPoint + [move[1]]
                    # problemPriorityQueue.push((move[0], newPathToPoint),1/move[0][0]**2)
                    problemPriorityQueue.push((move[0], newPathToPoint), problem.getCostOfActions(newPathToPoint))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
