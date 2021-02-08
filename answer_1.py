def server_cost(d1, m1, y1, d2, m2, y2):
    int cost

    #condition for checking the  server is deleted on the same day it is created
    
    if d1==d2 & m1==m2 & y1==y2:
	cost=20
    
    #conditions for checking the server is deleted after a day but still within a month
    
    elif d1==d2-1 & m1==m2 & y1==y2:
	cost=30
    elif m1==2 & d1==28 & m2==3 & d2==1:
	cost=30
    elif (m1==4 | m1==6 | m1==9 | m1==11) & d1==30 & d2==1 & (m2=m1+1):
	cost=30
    elif (m1==1 | m1==3 | m1==5 | m1==7 | m1==8 | m1==10 | m1==12) & d1==31 & d2==1 & (m2=m1+1):
	cost=30

    #conditions for checking the server is deleted after a month but still within a year
    
    elif m1==m2-1 & y1==y2:
	cost=1000*(m2-m1)
    elif y2==y1+1:
	cost=20000
    print(cost)
	
    return 0

if __name__ == '__main__':
    #created date
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])
    
    #deleted date
    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
