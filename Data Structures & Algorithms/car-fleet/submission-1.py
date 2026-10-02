class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedbypos = [(position[i], speed[i]) for i in range(len(position))]
        sortedbypos.sort(reverse = True)
        numfleets = 1
        curfintime = (target-sortedbypos[0][0])/sortedbypos[0][1]
        for i in range(1, len(position)):
            testfin = (target-sortedbypos[i][0])/sortedbypos[i][1]
            if testfin>curfintime:
                curfintime = testfin
                numfleets+=1
        return numfleets