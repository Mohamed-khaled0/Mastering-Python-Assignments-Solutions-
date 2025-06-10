# 1

get_score = {
    'Math' : '90',
    "Science":"80",
    "Language":"70"
}

def get_score(**subjects):
  for subject , score in subjects.items():
    print(f'{subject} => {score}')

get_score(Math=90, Science=80, Language=70)

print("-" * 100)



# 2
def get_people_scores(name="", **skills):
    if name:
        if skills:
            print(f"Hello {name} This Is Your Score Table:")
            for subject, score in skills.items():
                print(f"{subject} => {score}")
        else:
            print(f"Hello {name} You Have No Scores To Show")
    else:
        for subject, score in skills.items():
            print(f"{subject} => {score}")

get_people_scores("Osama", Math=90, Science=80, Language=70)

print("-" * 100)



# 3


scores_list = {
   'Math' : 90,
'Science' : 80,
'Language' : 70 
}

def get_the_scores(name="" , **scores_list) :
    if name != '' :
        print(f'Hello {name} This Is Your Score Table: ')
    for subject ,score in scores_list.items() :
        return(f"{subject} => {score}")


print(get_the_scores('Mohamed',**scores_list))
print(get_the_scores(**scores_list))