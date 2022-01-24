import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv(r"C:\Users\DELL\Downloads\ipl.csv")
data_new=data.drop([ 'season', 'byes', 'legbyes',
       'penalty', 'wicket_type', 'player_dismissed', 'other_wicket_type',
       'other_player_dismissed','noballs','wides'],axis=1)


#Calculating Total Runs
data_new['total runs'] = data_new['runs_off_bat'] + data_new['extras']



#Merging Delhi Capitals and Delhi Daredevils
#Merging Punjab Kings and Kings XI Punjab
data_new['batting_team']=data_new['batting_team'].apply(lambda x: 'Delhi Capitals' if x=='Delhi Daredevils' else x)
data_new['batting_team']=data_new['batting_team'].apply(lambda x: 'Punjab Kings' if x=='Kings XI Punjab' else x)
data_new['bowling_team']=data_new['bowling_team'].apply(lambda x: 'Delhi Capitals' if x=='Delhi Daredevils' else x)
data_new['bowling_team']=data_new['bowling_team'].apply(lambda x: 'Punjab Kings' if x=='Kings XI Punjab' else x)

#Merging the Duplicates
data_new['venue']=data_new['venue'].apply(lambda x:'M Chinnaswamy Stadium' if x=='M.Chinnaswamy Stadium' else x)
data_new['venue']=data_new['venue'].apply(lambda x:'MA Chidambaram Stadium' if (x=='MA Chidambaram Stadium, Chepauk')or(x=='MA Chidambaram Stadium, Chepauk, Chennai') else x)
data_new['venue']=data_new['venue'].apply(lambda x: 'Wankhede Stadium' if x== 'Wankhede Stadium, Mumbai' else x)


current_team=['Royal Challengers Bangalore', 'Kolkata Knight Riders',
       'Punjab Kings', 'Chennai Super Kings', 'Delhi Capitals',
       'Rajasthan Royals','Mumbai Indians','Sunrisers Hyderabad']

indian_stadium=['M Chinnaswamy Stadium', 'Feroz Shah Kotla','Eden Gardens', 'Wankhede Stadium',
       'MA Chidambaram Stadium','Sardar Patel Stadium, Motera', 'Arun Jaitley Stadium']

data_new = data_new[(data_new['batting_team'].isin(current_team)) & (data_new['bowling_team'].isin(current_team))& (data_new['venue'].isin(indian_stadium))]
data_edited=data_new[(data_new['ball']>=0.1)&(data_new['ball']<5.7)]

# data_edited[data_edited['ball']==5.6]
data_edited = data_edited.reset_index()
data_edited.drop(['index'],axis=1,inplace=True)
data_edited.head(50)
# data_edited.loc[data_edited['ball']==5.6]
a=[-1]
a.extend(list(data_edited.loc[data_edited['ball']==5.6].index))
runs=list(data_edited['total runs'])

#Calculating the ScoreBoard
score_board=[]
total_score=[]
for i in range(len(a)-1):
    b=0
    for j in range(a[i]+1,a[i+1]+1):
        b=b+runs[j]
        score_board.append(b)
    total_score.append(b)

data_edited['score']=score_board


data_edited.drop(['runs_off_bat','extras','total runs'],axis=1,inplace=True)


data_edited.to_csv("myPreprocessed.csv", index = False)
print(data_edited.head(10))
print('Aravinthan')