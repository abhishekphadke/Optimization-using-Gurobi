# Plot the solution to Euclidean covering problems
# Author: Antonio Medrano
import sys
import matplotlib.pyplot as plt
import numpy as np

def plotData(sites):
    
    mSize = 4
    
    plt.figure(figsize=(6,6))
    plt.plot(sites[:,1], sites[:,2], 'ko', markersize = mSize)
    plt.axis('equal')
    plt.show()

def plotSolution(sites, X, cols, SD):
    
    mSize = 4  # marker size
    
    plt.figure(figsize=(6,6))
    plt.plot(sites[:,1], sites[:,2], 'ko', markersize = mSize) # plot demands as black dots
    numSites = len(X)
    for j in range(numSites):
        if (X[j].x == 1.0): # plot located facilities as red dots with blue covering ranges
            plt.plot(sites[cols[j],1], sites[cols[j],2], 'ro', markersize = mSize)
            circle = plt.Circle((sites[cols[j],1], sites[cols[j],2]), SD, color='g', fill=False)
            plt.gcf().gca().add_artist(circle)
    
    plt.axis('equal')
    plt.show()
    
def plotSolutionE(sites, essential, X, cols, SD):
    
    mSize = 4
    
    plt.figure(figsize=(6,6))
    plt.plot(sites[:,1], sites[:,2], 'ko', markersize = mSize)
    numSites = len(X)
    for j in range(numSites):
        if (X[j].SolutionValue() == 1.0):
            plt.plot(sites[cols[j],1], sites[cols[j],2], 'bo', markersize = mSize)
            circle = plt.Circle((sites[cols[j],1], sites[cols[j],2]), SD, color='g', fill=False)
            plt.gcf().gca().add_artist(circle)
    for j in essential:
        plt.plot(sites[j,1], sites[j,2], 'ro', markersize = mSize)
        circle = plt.Circle((sites[j,1], sites[j,2]), SD, color='g', fill=False)
        plt.gcf().gca().add_artist(circle)
    
    plt.axis('equal')
    plt.show()
    
def plotTradeoff(file, solution):

    mSize = 2
    rows, cols = solution.shape

    plt.figure(figsize=(10,6))
    plt.step(solution[:,1], solution[:,0], where='pre')
    plt.plot(solution[:,1], solution[:,0], 'ko', markersize = mSize)
    plt.ylim(0, solution[rows-1,0]+1)
    plt.xlim(0, solution[0,1]+1)
    #plt.xscale('log')
    plt.ylabel('p-facilities')
    plt.xlabel('Service Distance')    
    plt.title('Complete P-Center Trade-Off Frontier, ' + file)
    plt.show()
    
    # plt.figure(figsize=(10,6))
    # plt.step(solution[:,0], solution[:,1], where='post')
    # plt.plot(solution[:,0], solution[:,1], 'ko', markersize = mSize)
    # plt.xlim(0, solution[rows-1,0]+1)
    # plt.ylim(0, solution[0,1]+1)
    # #plt.yscale('log')
    # plt.xlabel('p-facilities')
    # plt.ylabel('Service Distance')
    # plt.title('Complete P-Center Trade-Off Frontier')
    # #plt.axis('equal')
    # plt.show()

