def EuclideanDistance(start, end):
    """ Take 2 tuple as vector and return the Euclide distance between them """
    return ((end[0]-start[0]) ** 2 + (end[1]-start[1]) ** 2) ** 0.5

def SumDistance(vectors):
        sumDist = 0.0
        for i in range(len(vectors) - 1):
            sumDist  += EuclideanDistance(vectors[i], vectors[i+1])
        return sumDist