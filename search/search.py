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
#from searchAgents import PositionSearchProblem


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
    return  [s, s, w, s, w, w, s, w]
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
    specifiedActions = [] #Set of action that i will return to get the goal
    previouslyVisited = set() # I use it as a reference as not to visit a place twice
    previouslyVisited.add(problem.getStartState()) # add initial state as visited
    problemStack = util.Stack()
    problemStack.push(problem.getStartState())

    while not problem.isGoalState(problem.getStartState()): # while i could not achieve the goal
        nextPossilbeMoves = problem.getSuccessors(problem.getStartState()) # possible actions from my positions
        nextPossilbeMoves.sort(key=lambda t: t[2])  # sort possible actions alphapitically
        if not nextPossilbeMoves:
            # set current state to previous
            specifiedActions.pop()
            prevPositiionVisited = problemStack.pop()
            problem = searchAgents.PositionSearchProblem(problem.gameState, problem.costFn,problem.goal, prevPositiionVisited,problem.warn, problem.visualize)
            continue

        indexAction = 0
        # try to find the first index of list which is not visited, if all are visited; then go to except
        try:
            while (nextPossilbeMoves[indexAction][0]) in previouslyVisited:
                indexAction +=1
        except IndexError:
            # i will get to the last visited place
            specifiedActions.pop()
            print(specifiedActions)
            prevPositiionVisited = problemStack.pop()
            if prevPositiionVisited == problem.getStartState():
                prevPositiionVisited = problemStack.pop()
            # set problem to current state
            problem = searchAgents.PositionSearchProblem(problem.gameState, problem.costFn, problem.goal,
                                                         prevPositiionVisited, problem.warn, problem.visualize)
            continue

        firstAction = nextPossilbeMoves[indexAction]
        previouslyVisited.add(firstAction[0])
        problemStack.push(firstAction[0])
        # set current state to now
        problem = searchAgents.PositionSearchProblem(problem.gameState, problem.costFn,problem.goal, firstAction[0],problem.warn, problem.visualize)
        # add action to specified actoins
        specifiedActions.append(firstAction[1])
        # check if not visited
    print(specifiedActions)
    return specifiedActions

    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
