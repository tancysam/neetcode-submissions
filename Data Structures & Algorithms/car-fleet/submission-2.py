class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i],((target - position[i])/speed[i])])

        

        cars.sort(key=lambda x: x[0], reverse = True)



        print(cars)
        #Time = (target-pos)/speed

        stack = []
        counter = 0

        # Go through cars;
        # compare stack[-1][2] -> speed of last car in stack; if time taken is greater than current, means car can fleet up, append
        # else wipe stack; counter += 1; append current one and then continue with rest of list
        # return counter
        
        for i in range(len(cars)):
            if counter == 0 and len(stack)==0:
                stack.append(cars[0])
            elif stack[0][2] >= cars[i][2]:
                stack.append(cars[i])
            else:
                counter += 1
                stack = []
                stack.append(cars[i])
            print(stack)
        
        if len(stack) > 0:
            counter += 1
        
        return counter
            