"""A healthcare tech company has a number of activity records for each Health
Advocate (each "HA"). Each activity record is represented by a list of 3-element tuples:  
activity = [(timestamp, 'action', client), ...].  For example, (1, '@login', None) means this HA logged in to our system at time 1, 
(5, '@startVideo', 'Bob') means that this HA started a video stream with the client Bob 
at time 5.
Assumptions:
- Every HA can stream with a maximum of two clients at any moment.
- the tuples are listed sequentially based on timestamps
Task: 
- calculate both (A) the duration of HA's logged in time, e.g. the sum of 
all periods between '@login' and '@logout', and (B) the duration of HA's time 
spent simultaneously streaming video with two clients.
"""

activity = [(1, '@login', None),
(5, '@startVideo', 'Bob'),
(20, '@startVideo', 'Thomas'),
(66, '@stopVideo', 'Thomas'),
(70, '@startVideo', 'Lily'),
(75, '@stopVideo', 'Bob'),
(78, '@stopVideo', 'Lily'),
(100, '@logout', None),
(150, '@login', None),
(160, '@startVideo', 'Thomas'),
(205, '@stopVideo', 'Thomas'),
(210, '@logout', None) ]

def cal_durations(activity):
    A=0
    B=0
    for i in range(len(activity)-1):
        if activity[i][1] == '@login':
            logout = [x for x in activity[i:] if x[1] == '@logout'][0][0]
            A += (logout - activity[i][0])
        else:
            if activity[i][1] == '@startVideo':
                stop1 = [x for x in activity[i+1:] if (x[1] == '@stopVideo' 
                                                    and x[2] == activity[i][2])] [0][0]
                for j in range(i+1,len(activity)):
                    if activity[j][1] == '@startVideo' and activity[j][0]<stop1:
                        start2 = activity[j][0]
                        stop2 = [x for x in activity[j+1:] if (x[1] == '@stopVideo' 
                                                        and x[2] == activity[j][2])] [0][0]
                        if stop1 > stop2:
                            B += stop2 - start2;
                        else:
                            B += stop1 - start2
                
    return A, B
                    
A, B = cal_durations(activity)
print("HR's total login time = ", A)
print("HR's total video time with at least two clients = ", B)
            