class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        input: position - list of int, speed - list of int, LENGTH n, target - int
        - speed and position of the ith car
        output: return the number of DIFFERENT car fleets
        constraints: a car cannot pass (can be at same pos) another car, 
        car fleet is a nonzero set of cars driving at the same position and speed, 
        if car catches up to a fleet at the moment the fleet reaches dest. then its part of the fleet

        ex:
        target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        [x,x,_,_,x,_,_,x,_,_,_]

        each car can only go as fast as the one in front of it
        """
        def sortCars(car):
            return car[0]

        cars = [(a,b) for a,b in zip(position,speed)]
        cars.sort(reverse = True, key=sortCars)
        
        stack = [] # keep track of the times of each fleet
        
        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)



