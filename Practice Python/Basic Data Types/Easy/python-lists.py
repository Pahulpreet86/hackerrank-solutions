if __name__ == '__main__':
    N = int(input())
    commands=[]
    for _ in range(N):
        commands.append(input())
    data=[]
    for command in commands:
        
        actual_command=command.split()
        
        if actual_command[0]=="print":
            
            print(data)
            
        elif actual_command[0]=="insert":
            
            index=int(actual_command[1])
            
            integer=int(actual_command[2])
            
            data.insert(index,integer)
            
        elif actual_command[0]=="remove":
            
            integer=int(actual_command[1])
            
            data.remove(integer)
            
        
        elif actual_command[0]=="append":
            
            integer=int(actual_command[1])
            
            data.append(integer)
            
            
        elif actual_command[0]=="sort":
            
            data.sort()
            
        elif actual_command[0]=="pop":
            
            data.pop()
        
        elif actual_command[0]=="reverse":
            
            data.reverse()
        

