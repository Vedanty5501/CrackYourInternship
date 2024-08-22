class Solution:

    def findMinDiff(self, A,N,M):

        A.sort()
        minn=A[-1]
        for i in range(len(A)-M+1):
            diff = A[i+M-1]-A[i]
            if diff<minn:
                minn=diff
        return minn