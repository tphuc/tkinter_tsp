from mathDistance import EuclideanDistance, SumDistance
from random import sample

class NNRoute:

    @classmethod
    def Solve(NNRoute, Nodes):
        _Nodes = Nodes.copy()
        """ reorder list of Nodes visit, chosing the closet city each turn"""
        routeNodes = []
        # Initialize
        currentNode = _Nodes[0]
        routeNodes.append(currentNode)
        # remove the start of the Route
        _Nodes.remove(currentNode)
        # Iterate
        while len(routeNodes) != len(Nodes) and len(_Nodes):
            closetNode = NNRoute.closetSearch(currentNode, _Nodes)
            # Update list, current City
            currentNode = closetNode
            routeNodes.append(currentNode)
            _Nodes.remove(currentNode)
        return routeNodes

    @classmethod
    def closetSearch(NNRoute, startObj, targetObj_ls):
        """ 
        Take a StartObject and a list of TargetsObjects and calculate which one is closet
        return the Closet target
        """
        minDist = EuclideanDistance(targetObj_ls[0].loc, startObj.loc)
        closetTarget = targetObj_ls[0]
        # Iterate all targets
        for tObj in targetObj_ls:
            if EuclideanDistance(tObj.loc, startObj.loc) < minDist:
                minDist = EuclideanDistance(tObj.loc, startObj.loc)
                closetTarget = tObj
        return closetTarget
    

class LocalSearch:
    @classmethod
    def _Opt2swap(LocalSearch, Route, i, k):
        return Route[:i+1] + Route[k:i:-1] + Route[k+1:]

    @classmethod
    def Opt2Solve(LocalSearch, Route):
        bestDistance = SumDistance([node.loc for node in Route])
        for i in range(1,len(Route)-2):
            for k in range(i+1, len(Route) - 1):
                newRoute = LocalSearch._Opt2swap(Route, i, k)
                newDist = SumDistance([node.loc for node in newRoute])
                #print(i, k, str([c.name for c in newRoute]), newDist)
                if newDist < bestDistance:
                    Route = newRoute
        return Route
