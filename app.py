import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
	page_icon="soccer",
    page_title="Predictions",
    layout="wide",
)

mapping={
0:'Hasan',
1:'Ali',
2:'Abdul',
3:'Haedarah',
4:'Mahmoud'
}

data=pd.read_csv("Data/data.csv")
res=[["Hasan",0],["Ali",0],["Abdul",0],["Haedarah",0],["Mahmoud",0]]
standings=pd.DataFrame(res,columns=['Name','Pts'])

header=st.container()
st.write("""---""")
UpperBlock=st.container()
st.write("""---""")
LowerBlock=st.container()
st.write("""---""")
footer=st.container()





with header:
	col1,col2=st.columns([1,4],gap="large")

	with col1:
		st.image("Objects/pred.png",use_column_width=True)

	with col2:
		st.title("FIFA WORLD CUP QATAR 2022 Predictions Game - KIIT Version")
		st.write("Results will be calculated as follow:")
		st.write("- if you predict the same exact result +5.")
		st.write("- if you predict the result with the same difference of goals for your expected winner +3.")
		st.write("- if you predict it to be winning for a team and they win (without implementing first and second rules) +2.")
		st.write("- if you predict it to be winning for one of the teams and they tie -1.")
		st.write("- if you predict it to be draw and one of the teams wins -1.")
		st.write("- if you predict it to be winning for one of the teams and the other team wins -3.")
		st.write("")
		st.write("--Scores get refreshed after matches--")
		




with UpperBlock:

	st.header("Standings")
	col1,col2,col3=st.columns([1,1,1],gap="large")

	for i in range(5):
		a=data[data['Name']==mapping[i]]
		b=data[data['Name']=="REAL"]

		flag=2
		cur=0

		for j in a.columns:
			
			if flag==2:
				flag=0
				continue
			
			if flag==0:
				player_home=int(a[j])
				real_home=int(b[j])
				flag=1
			
			else:
				flag=0
				player_away=int(a[j])
				real_away=int(b[j])
				
				if real_home==1000:
					break
				
				elif player_home==real_home and player_away==real_away:
					cur+=5

				elif (player_home-player_away)==(real_home-real_away):
					cur+=3

				elif (player_home-player_away)*(real_home-real_away)>0:
					cur+=2

				elif (player_home-player_away)*(real_home-real_away)==0:
					cur-=1

				else:
					cur-=3
 				
		standings["Pts"][standings["Name"]==mapping[i]]=cur


	with col2:
		standings=standings.sort_values(by="Pts", ascending=False)
		standings=standings.set_index("Name")
		st.table(standings)





with LowerBlock:
	
	st.header("Predictions")
	col1,col2=st.columns([1,3],gap="large")
	
	with col1:
		name=st.selectbox("Choose a player to display his/her predictions",data['Name'][:-1])

	col11,col22=st.columns([1,1],gap="large")

	with col11:
		st.subheader("Predicted scores by "+name+":")

		line=""
		result=" ("
		flag=2
		idx=1

		a=data[data['Name']==name]
		alist=a.columns

		for i in a:
			if flag==2:
				flag=0
				continue

			if flag==0:
				flag=1
				line+=i
				line+=" "
				result+=str(int(a[alist[idx]]))
				result+="-"
				idx+=1

			else:
				flag=0
				line+=i
				line=line.split()
				line=line[1]+" - "+line[3]
				line=line.replace('[','')
				line=line.replace(']','')
				result+=str(int(a[alist[idx]]))
				result+=")"
				idx+=1
				st.write(line+result)
				line=""
				result=" ("

	with col22:
		st.subheader("Real scores:")
		b=data[data['Name']=="REAL"]
		blist=b.columns

		line=""
		result=" ("
		flag=2
		idx=1

		for i in b:
			if flag==2:
				flag=0
				continue

			if flag==0:
				flag=1
				line+=i
				line+=" "
				result+=str(int(b[blist[idx]]))
				if (int(b[blist[idx]])==1000):
					break
				result+="-"
				idx+=1

			else:
				flag=0
				line+=i
				line=line.split()
				line=line[1]+" - "+line[3]
				line=line.replace('[','')
				line=line.replace(']','')
				result+=str(int(b[blist[idx]]))
				result+=")"
				idx+=1
				st.write(line+result)
				line=""
				result=" ("


with footer:
	st.write("KIIT Predictions Game")

