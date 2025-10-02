class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles   
        extra_drunk = 0            
        
        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1  
            numExchange += 1                           
            extra_drunk += 1                           
        
        return total_drunk + extra_drunk