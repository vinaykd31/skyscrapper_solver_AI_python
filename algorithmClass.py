import sys
from settings import *

class algorithm:
    def __init__(self, clues, N):
        self.clues=clues
        self.N=N

        self.solutiongrid=[[0 for x in range(self.N)] for x in range(self.N)]
        self.size=N*N
        self.constraint_set = [set(range(1,N+1)) for i in range((N*N))]
        self.assignedCount=0
        self.d={}
        self.seqCount=0
    def dcheck(self):
        for i in range(len(self.constraint_set)):
            if len(self.constraint_set[i])==1:
                self.d[i]=True

    def run(self,state):
        if state == 0 :
            self.clueElemination()
            self.printit()
        elif state ==1:
            self.constraintProp()
            self.printit()
        elif state == 2:
            self.eliminationAssignment()
            self.printit()
        else:
            self.sequenceElimination()
            self.printit()
            print('number of sequence' , self.seqCount)
            # self.constraintProp()
            # self.eliminationAssignment()

        # while len(self.d) != 25:
        #     self.constraintProp()
        #     self.printit()
        #     self.eliminationAssignment()
        #     self.printit()
        #     self.sequenceElimination()
        #     self.dcheck()

        # for i in range(self.N * self.N):
        #     if len(self.constraint_set[i]) == 1:
        #         self.solutiongrid[i//self.N][i%self.N] = self.constraint_set[i].pop()

        # print(self.solutiongrid)
        # self.printit()
        # return self.solutiongrid
        return self.constraint_set

    ##  helper function for sequence elimination

    def generateSequence(self,clist):
        seqlist =[]
        # def helper(curlist,i):
        #     for x in clist[i]:
        #         if x in curlist:
        #             continue
        #         curlist.append(x)
        #
        #         if i == len(clist) -1 :
        #             seqlist.append(curlist)
        #         else:
        #             helper(curlist,i+1)
        #
        # helper([],0)
        queue=[]
        for x in clist[0]:
            queue.append([x])
        #print(queue)
        c=0
        while len(queue) !=0 :
            l=queue.pop(0)
            #print(l)
            c+=1
            if (len(l) == len(clist)):
                # print(l)
                seqlist.append(l)
            else:
                for x in clist[len(l)]:
                    #print(x)
                    if x not in l:
                        #print('if')

                        queue.append(l+[x])
                    else:
                        #print('else')
                        continue
        # print(c)
        # print(seqlist)
        self.seqCount+=len(seqlist)
        return seqlist

    def notsatisfy(self,seq,clue):
        visible=0
        max=0
        for x in seq:
            if x>max:
                visible=visible+1
                max=x

        if visible != clue:
            # print( seq, ' ', clue, ' ', visible )
            return True
        else:
            return False


    def sizeCheck(self,clist):
        for x in clist:
            if len(x) > 1:
                return False
        return True

    def sequenceElimination(self):
        for row in range(self.N):
            leftclue=self.clues[0][row][0]
            rightclue=self.clues[0][row][1]
            clist= [self.constraint_set[row*self.N + i] for i in range(self.N) ]
            if self.sizeCheck(clist):
                continue
            seqlist = self.generateSequence(clist)
            print(seqlist)
            for seq in seqlist:
                if (self.notsatisfy(seq,leftclue) or self.notsatisfy(seq[::-1],rightclue)):
                    seqlist.remove(seq)
            #print( seqlist )
            for i in range(self.N):
                s=set()
                for seq in seqlist:
                    s.add(seq[i])
                #print(s)
                self.constraint_set[row * self.N + i] = s

        self.printit()


            # print('vvvin\n\n')
            # print(seqlist)
        print( 'vvvin\n\n' )
        for col in range(self.N):
            leftclue=self.clues[1][col][0]
            rightclue=self.clues[1][col][1]
            clist= [self.constraint_set[col+ self.N*i ] for i in range(self.N) ]
            #print(clist , end = '  ')
            if self.sizeCheck(clist):
                continue
            seqlist = self.generateSequence(clist)
            #print(seqlist)
            for seq in seqlist:
                if (self.notsatisfy(seq,leftclue) or self.notsatisfy(seq[::-1],rightclue)):
                    seqlist.remove(seq)

            for i in range( self.N ):
                s = set()
                for seq in seqlist:
                    s.add( seq[i] )
                #print(s)
                self.constraint_set[col+ self.N*i ] = s

            #print(seqlist)
        #print( 'yes' )
        self.printit()
        self.constraintProp()
        self.eliminationAssignment()


    def isOnlyPossibleRowCol(self,index,ele):
        row = index//self.N
        col = index % self.N
        b = True
        for i in range(self.N):
            if i !=col and (ele in self.constraint_set[row*self.N + i]):
                b=False
        if b == True:
            return True
        b=True

        for i in range( self.N ):
            if i!=row and (ele in self.constraint_set[i*self.N + col]):
                b= False
        if b ==True:
            return True

        return False


    def eliminationAssignment(self):
        for i in range(len( self.constraint_set)):
            if len(self.constraint_set[i]) > 1:
                for x in self.constraint_set[i]:
                    if self.isOnlyPossibleRowCol(i,x):
                        self.constraint_set[i]={x}
                        self.constraintProp()
        print('After eliminationAssignment')

        # for i in range( len( self.constraint_set ) ):
        #     print( '%15s %2d' % (str( (self.constraint_set[i]) ), i))



    def constraintProp(self):
        print('\ni am in constraintProp')

        queue= []

        N=self.N
        for i in range(self.size):
            if len(self.constraint_set[i]) == 1 and i not in self.d:
                queue.append((i // N, i%N , self.constraint_set[i]))
                self.d[i]=True

        ## row, col

        while len(queue) !=0:
            (row,col,s ) = queue.pop(0)
            #print(row,col,s )
            for i in range(self.N):
                x = row* self.N + i
                if i != col:
                    self.constraint_set[x] = (self.constraint_set[x ]- s)
                    if len(self.constraint_set[x]) == 1  and x not in self.d:
                        #print( 'g' )
                        self.d[x]=True
                        queue.append( (row, i ,self.constraint_set[x]))

            for i in range( self.N ):
                x = col + self.N *i
                if i != row:
                    self.constraint_set[x] = (self.constraint_set[x] - s)
                    if len( self.constraint_set[x] ) == 1 and x not in self.d:
                        self.d[x] = True
                        queue.append( (i,col, self.constraint_set[x]))

         ### for testing





    def clueElemination(self):
        ## for row ##
        for row in range(self.N):
            for side in range(2):   # 0 for left, 1 for right
               clue=self.clues[0][row][side]
               print(clue)
               if clue >1 and clue < self.N:
                   for d in range(self.N):
                       for x in range(self.N - clue + d+2, self.N + 1 ):
                           if side == 0:
                                self.constraint_set[row*self.N + d ].discard(x)
                                #print('%d is removed from cell %d' %(x ,row*self.N + d))
                           else :
                               self.constraint_set[row * self.N + self.N - d -1].discard( x )
                               #print( '%d is removed from cell %d' % (x, row * self.N + self.N - d -1) )
               elif clue == 1:
                   if side == 0:
                       # print('here')
                       self.constraint_set[row*self.N]= {self.N}
                   else:
                       # print('nhere')
                       self.constraint_set[row * self.N + self.N -1]= {self.N}
               else:
                   if side == 0:
                       for i in range(self.N):
                            self.constraint_set[row*self.N+i]= {i+1}
                   else:
                       for i in reversed(range(self.N)):
                            self.constraint_set[row*self.N + i]={self.N-i}



           ## for col
        for col in range(self.N):
            for side in range(2):   # 0 for left, 1 for right
               clue=self.clues[1][col][side]
               print(clue)
               if clue >1 and clue < self.N:
                   for d in range(self.N):
                       for x in range(self.N - clue + d+2, self.N + 1 ):
                           if side == 0:
                                self.constraint_set[col+ self.N*d ].discard(x)
                                #print('%d is removed from cell %d' %(x ,col+ self.N*d))
                           else :
                               self.constraint_set[col + (self.N -1 -d)*self.N].discard( x )
                               #print( '%d is removed from cell %d' % (x, col +  (self.N -1 -d)*self.N ))
               elif clue == 1:
                   if side == 0:
                       #print( 'here' )
                       self.constraint_set[col]= {self.N}
                   else:
                       #print( 'here' )
                       self.constraint_set[col + (self.N - 1) * self.N]= {self.N}
               else:
                   if side == 0:
                       for i in range( self.N ):
                           self.constraint_set[i*self.N+col] = {i + 1}
                   else:
                       for i in reversed( range( self.N ) ):
                           self.constraint_set[col +self.N + i*self.N] = {self.N - i}
        for i in range( len( self.constraint_set ) ):
            if i % self.N == 0:
                print( ' ' )
            print( '%15s %2d' % (str( (self.constraint_set[i]) ), i), end=' ' )


    def printit(self):
        for i in range( len( self.constraint_set ) ):
            if i % self.N == 0:
                print( ' ' )
            print( '%15s %2d' % (str( (self.constraint_set[i]) ), i), end=' ' )
        print()

    def textToScreen(self, window, text, pos):
        fontObj = pygame.font.SysFont( "comicsansms", 25)
        font = fontObj.render( text, False, BLACK )
        # fontWidth = font.get_width()
        # fontHeight = font.get_height()

        window.blit( font, pos )
