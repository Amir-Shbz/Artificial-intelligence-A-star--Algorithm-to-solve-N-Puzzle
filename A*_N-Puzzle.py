import math

class Node():
    def __init__(self, numbers, f_score, level):
        self.numbers = numbers
        self.f_score = f_score
        self.level = level
     
    #--------------------------------------------------
    
    def find_blank(self):
        for i in range(0,len(self.numbers)):
             for j in range(0,len(self.numbers)):
                if self.numbers[i][j] == '*':
                     return i,j
    
    #--------------------------------------------------
    
    def move_space(self,x0,y0,x1,y1):
        l = len(self.numbers)
        if (x1>=0 and x1<l) and (y1>=0 and y1<l):
            a = []
            
            for i in self.numbers:
                t = []
                for j in i:
                    t.append(j)
                a.append(t)
                
            t = a[x1][y1]
            a[x1][y1] = a[x0][y0]
            a[x0][y0] = t
            return a
        else:
            return None  
    
    #--------------------------------------------------
    
    def children(self):
        i,j = self.find_blank()
        adj = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]
        children_list = []
        for k in adj:
            child = self.move_space(i,j,k[0],k[1])
            if child is not None:
                children_list.append(Node(child,self.level+1,0))
        return children_list   
  
  
  
class N_Puzzle():
    def __init__(self, N):
        self.N = N
        self.queue = []
        self.path = []
                    
    #--------------------------------------------------                
                    
    def get_state(self):
        data = []
        l = int(math.sqrt(self.N+1))
        for i in range(0,l):
            data.append(input().split(" "))
        return data
    
    #--------------------------------------------------
    
    def heuristic(self, current, goal):
        h = 0
        l = int(math.sqrt(self.N+1))
        for i in range(0,l):
            for j in range(0,l):
                if (current.numbers[i][j]!=goal.numbers[i][j]) and (current.numbers[i][j]!='*'):
                    h += 1
        return h    
    
     #--------------------------------------------------    
        
    def solve(self):
        print("Enter Start State : ")
        start = Node(self.get_state(),0 ,0)
        print("\n")
        print("Enter Goal State : ")
        goal = Node(self.get_state(),0 ,0)
        
        start.f_score = self.heuristic(start,goal) + start.level
        
        self.queue.append(start)
        
        print("\n\n\n")
        print("-------------------------------------")
        print("Start")
        print("\n")
        
        l = int(math.sqrt(self.N+1))
        while True:
            current = self.queue[0]
            
            for i in range(l):
                for j in range(l):
                    print(current.numbers[i][j], end="  ")
                print("\n")
                
            if self.heuristic(current, goal) == 0 :
                break
            
            print("\n")
            print("-------------------------------------")
            print("\n")
                    
            for i in current.children():
                i.f_score = self.heuristic(i,goal)
                self.queue.append(i)
                
            self.path.append(current)
            del self.queue[0]
            
            test_f = 0
            for i in range(0,len(self.queue)):
                if self.queue[i].f_score < self.queue[test_f].f_score:
                    test_f = i
            x = self.queue[0]
            self.queue[0] = self.queue[test_f]
            self.queue[test_f] = x        
        
