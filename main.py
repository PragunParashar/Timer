import time
hours = int(input('Enter the number of Hours: '))
minutes = int(input('Enter the number of Minutes: '))
seconds = int(input('Enter the number of Seconds: '))
seconds += (hours * 3600 + minutes * 60) 
while seconds >= 0:
    print (f'Hours: {seconds//3600:02} , Minutes: {(seconds%3600)//60:02} , Seconds: {(seconds%3600)%60:02}')
    seconds -= 1
    time.sleep (1)
print ('Time\'s up!')