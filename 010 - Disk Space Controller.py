#010 - Disk Space Controller

def byteToMB(lenBytes):
    lenBytes = float(lenBytes)
    Result = float(lenBytes/(1024**2))
    return Result

def percentPerUser(Data, total):
    Percent = (Data[3]/total)*100
    Data.insert((len(user)), Percent)

def UsedSpaceAverage(Data, total):
    Average = 0
    Items = len(Data)
    Average = total/(Items+1)
    return Average

while True:
    print('1-Start\n2-Quit')
    op = input('Answer: ')
    if op == '1':
        Value = 0
        pos = 1
        Total = 0
        Avg = 0
        try:
            FileName = open(input('File: '))
            Users = [line.split() for line in FileName]

            for user in Users:
                user.insert(0, pos)
                Value = byteToMB(float(user[2]))
                Total += Value
                user.insert((len(user)), Value)
                pos += 1
                
            for user in Users:
                percentPerUser(user, Total)
            
            New = 'Results.txt'
            NewFile = open(New, 'w')
            
            Avg = UsedSpaceAverage(user, Total)
            NewFile.write('ACME Inc --- Used Disk Space.\n')
            NewFile.write('N°\tUser\t       Used Space\tUsed Percent\n\n')
                
            for user in Users:
                Tax = f'{round(user[3],2):.2f}'
                Percent = '%.2f' %user[4]
                NewFile.write(str(user[0])+'\t'+'{:<9}'.format(user[1])+'\t'+'{:<10}'.format(Tax)+'MB'+'\t'+ '{:.2f}'.format(user[4])+'%'+'\n')
            NewFile.write(f"Used Disk Space[Total]: {Total:.2f}MB\n")
            NewFile.write(f"Used Disk Space[Average]: {Avg:.2f}MB\n")

            NewFile.close()

            Arq = open('Results.txt')
            print(Arq.read())
            
        except:
            print('Access Denied!')
    elif op == '2':
        print('Turn Off')
        break





