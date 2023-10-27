# valueIterationAgents.py
# -----------------------
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


import mdp, util
from collections import Counter
counter = Counter()

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
    * Please read learningAgents.py before reading this.*
    A ValueIterationAgent takes a Markov decision process (see mdp.py) on initialization and runs value iteration for a given number of iterations using the supplied discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Your value iteration agent should take an mdp on construction, run the indicated number of iterations and then act according to the resulting policy.
        :param mdp: The Markov decision process
        :param discount: The discount factor
        :param iterations: The number of iterations to run value iteration
        """
        # Store the input parameters as instance variables
        self.mdp = mdp
        self.discount = discount
        self.values = Counter()

        # Run the value iteration algorithm for the specified number of iterations
        self.runValueIteration(iterations)

    def runValueIteration(self, iterations):
        """
        Runs the value iteration algorithm for the specified number of iterations
        :param iterations: The number of iterations to run the algorithm
        """
        for i in range(iterations):
            # Create a new dictionary to store the values for each state
            newValues = Counter()

            # For each state, compute its new value
            for state in self.mdp.getStates():
                # If the state is terminal, set its value to 0
                if self.mdp.isTerminal(state):
                    newValues[state] = 0
                # Otherwise, compute the Q-value for each action and set the state's value to the maximum Q-value
                else:
                    qValues = []
                    for action in self.mdp.getPossibleActions(state):
                        qValues.append(self.computeQValueFromValues(state, action))
                    newValues[state] = max(qValues)

            # Update the values dictionary with the new values
            self.values = newValues

    def computeQValueFromValues(self, state, action):
        """
        Computes the Q-value for a state-action pair given the current values of the states
        :param state: The current state
        :param action: The current action
        :return: The Q-value for the state-action pair
        """
        qValue = 0
        # For each possible next state and its probability, compute the Q-value
        for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            # Compute the reward for the current state-action-next state transition
            reward = self.mdp.getReward(state, action, nextState)
            # Compute the discounted value of the next state
            qValue += prob * (reward + self.discount * self.getValue(nextState))
        return qValue

    def computeActionFromValues(self, state):
        """
        Computes the best action to take given the current values of the states
        :param state: The current state
        :return: The best action to take
        """
        bestAction = None
        bestValue = float("-inf")
        # For each possible action, compute the Q-value and choose the one with the maximum Q-value
        for action in self.mdp.getPossibleActions(state):
            qValue = self.computeQValueFromValues(state, action)
            if qValue > bestValue:
                bestAction = action
                bestValue = qValue
        return bestAction

    def getValue(self, state):
        """
        Returns the value of a state

        :param state: The state
        :return: The value of the state
        """
        # If the state is terminal, return 0
        if self.mdp.isTerminal(state):
            return 0
        # Otherwise, return the value of the state stored in the self.values Counter object
        else:
            return self.values[state]

    def getPolicy(self, state):
        """
        Returns the best action according to the agent's policy

        :param state: The state
        :return: The best action according to the agent's policy
        """
        # Use the computeActionFromValues method to compute the best action for the given state
        return self.computeActionFromValues(state)
