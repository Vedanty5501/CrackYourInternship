class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_sum = 0
        win = len(cardPoints)-k
        for i in range(0,win):
            window_sum+=cardPoints[i]
        mini_sum = window_sum
        for i in range(win,len(cardPoints)):
            window_sum = window_sum + cardPoints[i] - cardPoints[i-win]
            mini_sum = min(mini_sum,window_sum)
        return sum(cardPoints) - mini_sum