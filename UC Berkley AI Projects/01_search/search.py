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
from util import Stack
from util import Queue
from util import PriorityQueue

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    closed = set() # Initialize a set to keep track of the visited states.
    fringe = Stack() # Initialize the imported stack data structure to keep track of the states that need to be explored.
    initial_state = problem.getStartState() # Get the initial state from the problem.
    fringe.push((initial_state, [])) # Add the initial state to the fringe along with an empty list of actions to get there.

    # Loop while there are still unexplored states in the fringe.

    while not fringe.isEmpty(): 
        state, actions = fringe.pop() # Pop a state and its corresponding list of actions from the top of the fringe.

        if problem.isGoalState(state):
            return actions
        if state not in closed:
            closed.add(state)
            for successor_state, action, _ in problem.getSuccessors(state):
                successor_actions = actions + [action]
                fringe.push((successor_state, successor_actions))

    return None


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = Queue()
    initial_state = problem.getStartState()
    fringe.push((initial_state, []))

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions
        if state not in closed:
            closed.add(state)
            for successor_state, action, _ in problem.getSuccessors(state):
                successor_actions = actions + [action]
                fringe.push((successor_state, successor_actions))
    return None


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = PriorityQueue()
    initial_state = (problem.getStartState(), [], 0)
    fringe.push(initial_state, 0)

    while not fringe.isEmpty():
        node, actions, cost = fringe.pop()
        if problem.isGoalState(node):
            return actions
        if node not in closed:
            closed.add(node)
            for successor, action, step_cost in problem.getSuccessors(node):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                fringe.push((successor, new_actions, new_cost), new_cost)

    return []
    


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = PriorityQueue()
    initial_state = (problem.getStartState(), [], 0)
    h = heuristic(initial_state[0], problem)
    fringe.push(initial_state, h)

    while not fringe.isEmpty():
        node, actions, cost = fringe.pop()
        if problem.isGoalState(node):
            return actions
        if node not in closed:
            closed.add(node)
            for successor, action, step_cost in problem.getSuccessors(node):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                h = heuristic(successor, problem)
                fringe.push((successor, new_actions, new_cost), new_cost + h)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
