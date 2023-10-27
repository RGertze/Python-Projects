# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]
    """
    def getRemainingFood(gameState):
     #This function extracts the food from the current game state and returns a list of (x,y) tuples
     
      food = gameState.getFood()
      food_list = food.asList()
      return food_list
    
    def getRemainingPowerPellets(gameState):
      
        #This function extracts the remaining power-ups from the current game state and returns it as a list of (x,y) tuples.
      
        powerPellets = gameState.getPowerPellets()
        return powerPellets
    
    def calculate_distance_to_nearest_powerPellet(gameState, position):
        
        #This function calculates the distance from the given position to the nearest power-up using the maze distance.
       
        powerPellets = gameState.getPowerPellets()
        if len(powerPellets) == 0:
          return 0
        distances = [util.manhattanDistance(position, powerPellets) for powerPellets in powerPellets]
        return min(distances)
    
    def get_distance_to_nearest_ghost(gameState, pos):
    
      #Returns the Manhattan distance to the nearest ghost (not counting scared ghosts) from the given position.
    
        minDistance = float('inf')
        for ghostState in gameState.getGhostStates():
            if not ghostState.scaredTimer:
                distance = manhattanDistance(pos, ghostState.getPosition())
                if distance < minDistance:
                    minDistance = distance
        return minDistance
    
    def get_num_food_in_radius(gameState, pos, radius):
       
        #Returns the number of remaining food dots within the given radius around the given position.
     
        foodGrid = gameState.getFood()
        x, y = pos
        num_food = 0
        for i in range(x - radius, x + radius + 1):
            for j in range(y - radius, y + radius + 1):
               if foodGrid[i][j]:
                num_food += 1
        return num_food
      """
    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
       
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        powerPellets = successorGameState.getCapsules()

        # calculate the evaluation score
        score = successorGameState.getScore()

        # calculate the remaining food pellets
        foodLeft = len(newFood.asList())

        # penalize the score based on the number of remaining food pellets
        if foodLeft == 0:
            score += 1000
        else:
            score -= foodLeft

       # calculate distance to closest food pellet
        foodDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        if len(foodDistances) > 0:
             minFoodDistance = min(foodDistances)
        else:
            minFoodDistance = 1
        score += 1 / minFoodDistance
    
      # calculate distance to closest ghost
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        if len(ghostDistances) > 0:
            minGhostDistance = min(ghostDistances)
        else:
            minGhostDistance = 0
        if minGhostDistance <= 1 and sum(newScaredTimes) == 0:
            score -= 1000
        elif minGhostDistance <= 2 and sum(newScaredTimes) == 0:
            score -= 500
        elif minGhostDistance <= 3 and sum(newScaredTimes) == 0:
            score -= 100
        else:
            score += 1 / minGhostDistance
            score += sum(newScaredTimes)

       # check if power pellets are available
        if powerPellets:
            powerDistances = [manhattanDistance(newPos, pellet) for pellet in powerPellets]
            minPowerDistance = min(powerDistances)
            minPowerDistance = min(powerDistances)
            if currentGameState.getNumFood() == 20:
                score += 1 / minPowerDistance
            elif currentGameState.getNumFood() == 116:
                score += 2 / minPowerDistance
            else:
                minPowerDistance = float("inf")
    
        return score
        """
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newPowerPellets = successorGameState.getPowerPellets()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        # Get remaining food
        remainingFood = remainingFood(successorGameState)
        
        # Get remaining power pellets
        remainingPowerPellets = remainingPowerPellets(successorGameState)
        
        # Calculate distance to nearest power pellet
        distanceToPowerPellet = distanceToPowerPellet(successorGameState, newPos)
        
        # Calculate distance to nearest ghost
        distanceToGhost = distanceToGhost(successorGameState, newPos)
        
        # Calculate number of food dots within a certain radius
        foodRadius = 3
        numFoodInRadius = numFoodInRadius(successorGameState, newPos, foodRadius)
        
        # Calculate the total number of food dots remaining
        numFood = len(remainingFood)
        
        # Calculate the total number of power pellets remaining
        numPowerPellets = len(remainingPowerPellets)
        
        # Calculate the score
        score = successorGameState.getScore()
        
        # Add weights to the features and return the evaluation score
        evaluation = score + (-1 * numFood) + (-10 * numPowerPellets) + (-2 * distanceToPowerPellet) + (-2 * distanceToGhost) + (2 * numFoodInRadius)
        
        return evaluation

        return currentGameState.getScore()
"""

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """
    
    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MyAgent(MultiAgentSearchAgent):
    def scoreEvaluationFunction(self, gameState):
        """
          This default evaluation function just returns the score of the game.
          The score is the same one displayed in the Pacman GUI.

          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        return gameState.getScore()

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def maxValue(gameState, agentIndex, depth):
              if gameState.isWin() or gameState.isLose() or depth == 0:
                  return self.evaluationFunction(gameState)
              v = float("-inf")
              for action in gameState.getLegalActions(agentIndex):
                  successor = gameState.generateSuccessor(agentIndex, action)
                  v = max(v, minValue(successor, agentIndex + 1, depth))
              return v

        def minValue(gameState, agentIndex, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            v = float("inf")
            for action in gameState.getLegalActions(agentIndex):
                successor = gameState.generateSuccessor(agentIndex, action)
                if agentIndex == gameState.getNumAgents() - 1:
                    v = min(v, maxValue(successor, 0, depth - 1))
                else:
                    v = min(v, minValue(successor, agentIndex + 1, depth))
            return v

        legalActions = gameState.getLegalActions(0)
        scores = []
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            scores.append(minValue(successor, 1, self.depth))
        bestScore = max(scores)
        bestIndices = [index for index, score in enumerate(scores) if score == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalActions[chosenIndex]
            

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
       
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # Setup information to be used as arguments in evaluation function
    pacman_position = currentGameState.getPacmanPosition()
    ghost_positions = currentGameState.getGhostPositions()

    food_list = currentGameState.getFood().asList()
    food_count = len(food_list)
    capsule_count = len(currentGameState.getCapsules())
    closest_food = 1

    game_score = currentGameState.getScore()

    # Find distances from pacman to all food
    food_distances = [manhattanDistance(pacman_position, food_position) for food_position in food_list]

    # Set value for closest food if there is still food left
    if food_count > 0:
        closest_food = min(food_distances)

    # Find distances from pacman to ghost(s)
    for ghost_position in ghost_positions:
        ghost_distance = manhattanDistance(pacman_position, ghost_position)

        # If ghost is too close to pacman, prioritize escaping instead of eating the closest food
        # by resetting the value for closest distance to food
        if ghost_distance < 2:
            closest_food = 99999

    features = [1.0 / closest_food,
                game_score,
                food_count,
                capsule_count]

    weights = [10,
               200,
               -100,
               -10]

    # Linear combination of features
    return sum([feature * weight for feature, weight in zip(features, weights)])
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

