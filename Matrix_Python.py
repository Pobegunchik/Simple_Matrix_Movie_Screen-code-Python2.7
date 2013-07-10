
import time
import random
size = 30
a = []

nums = [' ',0,1]
for i in range(size):
    a.append(nums[random.randint(0,2)])
while(1):
    for i in range(size-1):
        if a[i] == 0 or a[i]== 1:
            if random.randint(0,100)%10 == 0:        #every 10 or so we make one blank
                a[i] = nums[0]
            if random.randint(0,100)%5 == 2:         #about every 5 or so we switch from 0 -> 1 or 1->0
                if a[i] == 0:
                    a[i] = 1
                else:
                     a[i] = 0
            else:
                b = 0
        if a[i] == ' ':
            if random.randint(0,100) > 80:              #used to hold blank spaces together 
                a[i] = nums[random.randint(1,2)]
        

    print ' '.join(map(str,a))
        #a[i],''.join(map(str,a[i+1:]))
    time.sleep(0.08)
    
        
