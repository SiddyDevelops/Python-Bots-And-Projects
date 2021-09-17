import os 

def make_commit(days: int):
    if(days < 1):
        #Push
        return os.system('git push origin main')
    else:
        dates = f'{days} days ago'

        with open('bot.txt','a') as file:
            file.write(f'{dates}\n')

        #Staging
        os.system('git add bot.txt')

        #Commit
        os.system('git commit --date="'+ dates +'" -m "Regulate -v"')              

        return days * make_commit(days-1)

make_commit(10)        