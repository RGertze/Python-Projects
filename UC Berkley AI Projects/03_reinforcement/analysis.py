# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.
import os

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 0.5
    answerNoise = 0
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    answerDiscount = 0.5
    answerNoise = 0.1
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = -0.1
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    answerDiscount = 0
    answerNoise = 0.1
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward

def question6():
    answerEpsilon = None
    answerLearningRate = None

    for epsilon in [0, 0.1, 0.2, 0.3, 0.4, 0.5]:
        for learning_rate in [0.1, 0.2, 0.3, 0.4, 0.5]:
            # Run the experiment
            command = f"python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e {epsilon} -l {learning_rate}"
            output = os.popen(command).read()
            
            # Check if optimal policy was learned
            if "*** The optimal policy has been found! ***" in output:
                answerEpsilon = epsilon
                answerLearningRate = learning_rate
                break
        
        if answerEpsilon is not None:
            break
    
    if answerEpsilon is None:
        return 'NOT POSSIBLE'
    else:
        return answerEpsilon, answerLearningRate


if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
