from random import randint
from colorama import Fore,init
init(autoreset=True)
import pytube
from media import Media
from film import Film
from series import Series
from document import Document
from Clip import Clip
from media import Actor

ACTORS=[]
CASTS=[]
CLIP=[]
new_cast_list=[]

def read_from_database():
    actors=open("Project Media\db_actors.txt", "r")
    for line in actors:
       result=line.split(',')
       obj_actor=Actor(result[0], result[1], result[2])
       ACTORS.append(obj_actor)        
    actors.close()

    media=open("Project Media\db_clip.txt", "r")
    for line in media:
       result=line.split(',')
       for obj in ACTORS:
           if int(obj.media_id)==int(result[0]):
               CASTS.append(obj)     

       obj_clip=Clip(result[0], result[1], result[2], result[3], result[4], result[5], CASTS, result[7], result[8])
       CLIP.append(obj_clip)
       
    media.close()                         
read_from_database()

@staticmethod
def add():
            id=input("enter id : ")
            name=input("enter name : ")
            director=input("enter director : ")
            imdb=input("enter IMDB_Score : ")
            url=input("enter url : ")
            duration=input("enter duration : ")
            casts=input("enter casts (Separator : +) : ")
            genre=input("enter genre : ")
            writer=input("enter writer : ")
            new_clip=Clip(id, name, director, imdb, url, duration, casts, genre, writer)
            CLIP.append(new_clip) 

            list_casts=casts.split("+")
            for cast in list_casts:
                random_number=randint(1, 1000)
                id_cast=str(random_number)
                cast=Actor(id_cast, cast, id)
                new_cast_list.append(cast)
                
def edit():
    user_input=input("Enter Your Id Clip: ")
    for clip in CLIP:
        if user_input==clip.id: 
            print(Fore.RED+"-----------------------------------------")
            print(f"{' Name':5}", f"{' Director':8}", f"{' IMDB':10}")
            print(f"{clip.name:5}", f"{clip.director:8}", f"{clip.imdb:10}")
            print(Fore.RED+"-----------------------------------------")
            print(Fore.BLUE+"1_""Name""\n""2_""Director""\n""3_""IMDB")

            field_number=int(input("Enter the desired field to edit :"))
            if field_number==1:
                    new_name=input("Enter New Name :")
                    clip.name=new_name
                    print(Fore.GREEN+"The name of the desired clip was edited") 
                    break
            if field_number==2:
                    new_director=input("Enter New Director :")
                    clip.director=new_director
                    print(Fore.GREEN+"The name of the desired director was edited") 
                    break
            if field_number==3:
                    new_imdb=input("Enter New IMDB :")
                    clip.imdb=new_imdb
                    print(Fore.GREEN+"The desired IMDB was edited") 
                    break  
    else:
        print(Fore.RED+" ** (( Not Found  )) ** ")        

def remove():
    user_input=input("Enter Your Id : ")
    for clip in CLIP:
        if user_input==clip.id: 
            del clip
            print(Fore.RED+"The desired clip was deleted") 
            break
    else:
          print("(( Not Found  ))")

def search():
    first_Minute=int(input("Enter Your First Minute : "))
    second_Minute=int(input("Enter Your Second Minute : "))
    for clip in CLIP:
        temp=(clip.duration).split(":")
        duration=(int(temp[0])*60)+int(temp[1])
        if first_Minute < duration < second_Minute: 
            print(clip.name)
            break
    else:
        print(" ** (( Not Found  )) ** ")

def show_media():
     
    for clip in CLIP:
        print(Fore.YELLOW+f"{'Name':15}", Fore.YELLOW+f"{'Director':15}", Fore.YELLOW+f"{'IMDB':10}", 
              Fore.YELLOW+f"{'Duration':10}")
        print(f"{clip.name:15}", f"{clip.director:15}", f"{clip.imdb:10}",  f"{clip.duration:10}")
        print(Fore.YELLOW+f"{'Actors : ':10}")
        for actor in ACTORS:
         if int(clip.id)==int(actor.media_id):
            print(actor.actor_name)
        print(Fore.RED+"=====================================================================")   

def download_clip():
    clip_name=input("Please Enter Clip_name : ")
    for clip in CLIP:
        if clip_name==clip.name:
            clip.download(clip.url, clip.name)
        

def write_to_database():
    c=open("Project Media\db_actors.txt", "a")
    for item in new_cast_list:
        id=item.id
        actor_name=item.actor_name
        media_id=item.media_id
        c.write("\n"+id + ", " +actor_name + ", "+media_id)
    c.close()

    f=open("Project Media\db_clip.txt", "a")
    for clip in CLIP:
            id=clip.id
            name=clip.name
            director=clip.director
            imdb=clip.imdb
            url=clip.url
            duration=clip.duration
            casts=clip.casts
            genre=clip.genre
            writer=clip.writer
            
    f.write("\n"+id + ", " +name + ", "+director+ ", "+imdb+ ", "+url+ ", "+duration+ ", "+casts+ ", "+genre+ ", "+writer)
    f.close()                


def show_menue():
    print("1_ Add")
    print("2_ Edit")
    print("3_ Remove") 
    print("4_ Search")
    print("5_ Show Media")
    print("6_ Download_Clip")
    print("7_ Save & Exit")
    

while True:
    show_menue()
    choice=int(input(Fore.GREEN+ "Enter Your Choice : "))

    if choice==1:
         add()

    elif choice==2:
         edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
      show_media()
    elif choice==6:
      download_clip()  
    elif choice==7:
        write_to_database()
        exit(0)  
    else:
        print(Fore.RED+ "Please Choose Correctly ! \n \t \t \t Try Again . . . ")    