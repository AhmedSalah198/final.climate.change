import numpy as np
import pandas as pd
import streamlit as st
import datetime,requests
import plotly.express as px
from plotly import graph_objects as go



st.set_page_config(page_title='AHMED SALAH WEATHER', page_icon="☀️")
#st.markdown("<h1 style='text-align: center; font-size: 45px;'>full project video </h1>", unsafe_allow_html=True)

#Video
#st.video('ask.mp4')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')



#Disply Introduction Data
#st.write("<h1 style='text-align: center; font-size: 20px;'>Hi EPSILON </h1>", unsafe_allow_html=True)
#st.write("<h1 style='text-align: center; font-size: 20px;'> It's Me Again Ahmed Salah, First I'd Like To Thank Eng/Ahmed Moustafa For Being Such A Good Teacher And Brother For All Of Us .And I'd Like To Thank Ebsilon It For The Great Dibloma And It Was A Great 12 Months With You </h1>", unsafe_allow_html=True)


#st.write("<h1 style='text-align: center; font-size: 20px;'>Hi Ebsilon </h1>", unsafe_allow_html=True)
#st.write("<h1 style='text-align: center; font-size: 20px;'> It's Me Again Ahmed Salah First I'd Like To Thank Eng/Ahmed Moustafa For Being Such A Good Teacher And Brother For All Of Us .And I'd Like To Thank Ebsilon It For The Great Dibloma And It Was A Great 12 Months With You </h1>", unsafe_allow_html=True)



#st.write("It's Me Again Ahmed Salah, First I'd Like To Thank Eng/Ahmed Moustafa For Being Such A Good Teacher And Brother For All Of Us .And I'd Like To Thank Ebsilon It For The Great Dibloma And It Was A Great 12 Months With You")


#st.markdown('----')
#st.write("<h1 style='text-align: center; font-size: 20px;'> AND BEFORE YOU START READING I'd Like You To put your City In This Box, And Answer A Very Important Question  </h1>", unsafe_allow_html=True)



st.markdown('----')
#Display the Page Title
Page_Title= st.markdown("<h1 style='text-align: center; font-size: 45px;'>Climate Change - Global Warming</h1>", unsafe_allow_html=True)
Page_Title= st.markdown("<h1 style='text-align: center; font-size: 45px;'>( THERE'S NO PLANET B )</h1>", unsafe_allow_html=True)


#Display the Page Subtitle
st.markdown("<h1 style='text-align: center; font-size: 25px;'> By (Ahmed Salah Khalil)</h1>", unsafe_allow_html=True)
st.markdown('----')




# Load the image
image = st.image("Screenshot_1.png")
image = st.image("11.jpg")

st.markdown('----')

#Display Introduction
st.markdown("<h1 style='text-align: center; font-size: 30px;'>Content</h1>", unsafe_allow_html=True)

st.write("1- introdution")
st.write("2- Objectives")
st.write("3- data set")
st.write("4- data handling")
st.write("5- Exploratory data analysis") 
st.write("8- what will future climate be like")
st.write("7- conclusion")
st.write("8- Weather App Forecast")
st.write("9- Resources")

#introdution part
st.markdown("<h1 style='text-align: center; font-size: 30px;'>01- INTRODUCTION</h1>", unsafe_allow_html=True)



st.write("### Malaysia firms plunder sunken wrecks for rare steel used to make sensitive medical, scientific equipment")

st.image("112.png")
st.image("11 (2).png")


st.write("Pre-atomic age metal only found under the sea PETALING JAYA Low-background steel is steel manufactured before the atomic age.It was manufactured prior to (1945), when the atmosphere became contaminated by the atomic bombings of Hiroshima and Nagasaki during World War II,sciene then there was (2050) testes for nuclura recations and subsequent nuclear testing during the Cold War.Global steel production has since seen an increase in radioactivity in the metal.This radioactivity affects metal used for ultra-sensitive scientific and medical instruments and equipment, producing inaccurate readings.Prior to 1945, steel was used in the process of putting the iron together to form structures or sheets.This kind of steel is very much in demand, a source said.The only problem is, almost all non-interference steel lies on the ocean floor, in the form of ships sunk before 1945.The old sunken ships were not exposed to the air of the atomic age,said the source.This old metal is recycled and used to manufacture instruments used in medicine, light and radioactivity detection, and space exploration.")
st.image("11 (3).png")
st.image("11 (4).png")

st.write("The past two decades have painted a sobering picture of our planet's changing climate. Since the year 2000, we've witnessed undeniable evidence of a warming world, with the consequences rippling across ecosystems, societies, and economies. Let's delve into the key trends and impacts that have marked this critical period")


st.write("""

### Temperature Rise

* Global average temperature has increased by 0.6°C since 2000, with the last seven years being the hottest on record.
* This warming has led to melting glaciers, intensifying heatwaves, and disrupted weather patterns.
""")

st.image("45.png")


st.write("""

### Rising Seas

* Sea levels have risen by an average of 3 inches globally, posing a threat to coastal communities and infrastructure.
* The melting of polar ice sheets and glaciers is a major contributor to this rise.""")


st.image("54.png")


st.write("""

### Extreme Weather

* The frequency and intensity of extreme weather events like heatwaves, droughts, floods, and wildfires have increased significantly.
* These events cause devastation, displace communities, and inflict billions of dollars in damage.""")

st.image("11 (1).png")







#Video Formating
#st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Global wormaing video</h1>", #unsafe_allow_html=True)
#st.video('ask.mp4')



st.markdown("-----")
st.markdown("<h1 style='text-align: center; font-size: 30px;'>02- OBJECTIVES</h1>", unsafe_allow_html=True)
image = st.image("22.jpg")
st.write("1 -TO COLLECT AND CLEAN THE HUGE WEATHER DATA FROM (1749-2013)")
st.write(" 2 - TO EXPLORE AND ANALYZE THE DATA ")
st.write("3  - TO PREDICT FUTURE CLIMATE PATTERN")
st.write("4  - TO MAKE WEATHER APP FORECAST")


st.markdown("------")
st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>03 -DATASET</h1>",unsafe_allow_html=True)



#Disply Introduction Data
st.write(" This Time Coming With New Added Data Collected By Noaa And also Using The Data From Kaggle ")



image = st.image("33.jpg")

st.write(" I'll Tell You How I Got This Data From NOAA In This Video Below ")



#st.write(" i hope in this project we will discover some thigith new  مقاطع المناخ الدحيح")
st.video('vid22.mp4')
st.write("So Im Gonna Work With Both Data Collected From Noaa And From Kagelle")

st.write("-          8 CSV Files")
st.write("-         (8,700,212) ROWS")
st.write("-      37 FEATURES")
st.write("- Date: from NOAA Starts from 1909 to 1957 in Egypt collected from the GOVERNMENT WEATHER MONITORING CAIRO EZBEKIYA, EG	 ")
st.write("- Date: from Kaggle starts in 1750 for average land temperature and 1850 for max and min land temperatures and global ocean and land temperatures")
st.write("- LandAverageTemperature: global average land temperature in Celsius LandAverageTemperatureUncertainty: the 95% confidence interval around the average")
st.write("- LandMaxTemperature: global average maximum land temperature in Celsius")
st.write("- LandMaxTemperatureUncertainty: the 95% confidence interval around the maximum land temperature")

st.markdown("------")

st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>04 - DATA WRANGLING</h1>",unsafe_allow_html=True)
st.write(" - Load and explore ")
image = st.image("44.png")
image = st.image("Screenshot_4.png")
st.write(" - clean ")
image = st.image("55.png")
image = st.image("66.png")

image = st.image("Screenshot_5.png")
st.write(" - Feature extract and transform")
image = st.image("Screenshot_4.png")

st.markdown("-----")

st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>05 - EXPLORATORY DATA ANALYSIS </h1>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Questions should be answered after running this analysis</h1>",unsafe_allow_html=True)
st.write(" - Did the world increase in temperature?")
st.write(" - what are the hottest countries? ")
st.write(" - comparing important countries ")
st.write(" - are the hottest countries increased in temp more than the coler ones ?")
st.write(" - by how much is that increase ?")
st.write(" - When did the Global Warming Start ?")
st.write(" - Why 1975 exactly?")
st.write(" - lets study 1975 much more ")
st.write(" - what is the AverageTemperature in egypt ? ")
st.write(" - what is the hotest mounth in egypt ? ")
st.write(" - what is the future climate will be like ? ")









# Define the questions and their corresponding chart types
questions = {
    "Did the world increase in temperature?": "1.png",
    "what are the hottest countries?": "2",
    "comparing important countries": "Chart_3",
    "are the hottest countries increased in temp more than the coler ones ?": "Chart_4",
    "by how much is that increase ?": "Chart_5",
    "When did the Global Warming Start ?": "Chart_6",
    "Why 1975 exactly?": "Chart_7",
    "lets study 1975 much more": "Chart_8",
    "what is the AverageTemperature in egypt ?": "Chart_9",
    "what is the hotest mounth in egypt ?": "Chart_10",
    "what is the future climate will be like ?": "Chart_11"
}

st.markdown("-----")



# Display the dropdown list
st.write("<h3 style='font-weight: bold;'>Select Yor Question:</h2>", unsafe_allow_html=True)
question = st.selectbox("", list(questions.keys()))





# Display the chart based on the selected question
if question == "Did the world increase in temperature?":
    st.image("1.png")
    
    
    
    
elif question == "what are the hottest countries?":
    st.image("2.png")
    st.image("22.png")

    
    
    
    
    
    
elif question == "comparing important countries":
    st.image("3.png")
    
    
    
    
    
elif question == "are the hottest countries increased in temp more than the coler ones ?":
    st.image("4.png")

    
    
    
    
    
    
elif question == "by how much is that increase ?":
    st.image("5.png")
    st.write("- Brazil and Argentina - BIG deforestation issues (their wildfires have     increased big time and the decrease in agriculture is the main factor)")
    st.write("- Kazakhstan - a place for testing biological and nuclear weapons by the Soviets. Also, here are located the most polluting industries. Most of their water is infected by industrial and agricultural runoff and it is in some places radioactivity")
    
    
    
    
    
elif question == "When did the Global Warming Start ?":
    st.image("6.png")
    
    
    
    
    
    
    
elif question == "Why 1975 exactly?":
    st.image("7.png")

    st.write("- No doubt the Industrial Revolution but especially when the human discover Freon and that had an effect between 1900 and 1975.")
    st.write("- combining with the population increase that started somewhere in 1975 (from ~2.5 bil in 1950 to 5 bil in 2000)created an enormous overall global warming state.")

    
    
    
    
    
    
    
    
    
elif question == "lets study 1975 much more":
    st.image("8.png")
    st.image("122112.png")

    
    st.write("- I feel like 1975 was a (no turning back) point, so I chose this moment to compare temperatures before and after.")
    st.write("- Land Average Temperature - an increase from 8.37 degrees to 9.20; almost 1 full grade")
    st.write("- Land Maximum Temperature - an increase from 14.18 degrees to 14.89; 0.71 grades increase")
    st.write("- Land Minimum Temperatures - an increase from 2.45 degrees to 3.64; 1.19 grades increase")
    st.write("- The (Cold Weather) getting hotter more rapidly than the (Hot Weather) ")
    






elif question == "what is the AverageTemperature in egypt ?":
    st.image("9.png")
    st.image("99.png")


    
    
    
    
    
    
elif question == "what is the hotest mounth in egypt ?":
    st.image("10.png")

     
     
     
     
     

elif question == "what is the future climate will be like ?":
    st.image("77.png")
    st.write(" Right now the global temperature average is about (15) degrees Celsius, Based on the prediction, at (200) years the ML model predicted we could see a change in (+27.5) degrees Celsius  and at (500) years we would be sitting at around a (40) degrees Celsius global average and at (1000) years we would be sitting at around a (60) degrees Celsius global average ")
    
    
    
    
st.markdown("-----")



st.markdown("<h1 style='text-align: center ; font-size: 30px;'>07 - But what really future climate will be like</h1>", unsafe_allow_html=True) 


st.write("Predicting the future climate is a complex task, as it's influenced by numerous factors and uncertainties. However, based on current scientific understanding and climate models, here's a glimpse into what the future climate might hold: ")
st.image("7.png")

st.write("Temperature rise: The Earth's average temperature is projected to rise depending on our mitigation efforts. This warming will be unevenly distributed, with some regions experiencing significantly higher increases than others. ")









st.markdown("-----")


#Conclusion Data

st.markdown("<h1 style='text-align: center ; font-size: 30px;'>06 - Conclusion</h1>", unsafe_allow_html=True)    

st.write("- After the industrial revolution in 1975, the planet Earth experienced a continuous rise in temperatures, But when the world began to notice rising temperatures, it was too late")    
st.image("474.png")
st.image("5555.png")

st.write("- Therefore, in 2015, the Cop21 Climate Conference was held, if they set a condition that we limit the global temperature rise to 1.5 degree Celsius.") 
st.image("74.jpg")

st.write("- But something happened that was not desirable to happen, and the temperature is now increasing by 2 degree annually") 
st.image("44 (4).png")

st.write("-And that what was duscused in cop28 in dubai 2023 this year it was just only to keeb the 2 degree not to set limit to 1.5") 
st.image("666.jpg")

st.write("- But i ahmed salah think there is no hope  ") 
st.image("777.jpg")

st.write("- cause if we have to make someone think we have to make it with the two largest countries which are really in a big industrial war  ") 
st.image("74.png")


st.write("- And also as i said before Nuclear reaction experiments must be stopped ") 
#st.image("11.jpg")

st.markdown("-----")




#-----------------------------------------------




#-----------------------------------------------------------------------


st.markdown("-----")


#Conclusion Data

st.markdown("<h1 style='text-align: center ; font-size: 30px;'>09- Resources</h1>", unsafe_allow_html=True)    

st.write("- https://www.straitstimes.com/asia/se-asia/malaysia-firms-plunder-sunken-wrecks-for-rare-steel-used-to-make-sensitive-medical")   
 
st.write("- https://edition.cnn.com/2019/10/25/weather/medicane-mediterranean-storm-egypt-israel-wxc/index.html")  
st.write("- https://edition.cnn.com/2015/12/12/world/global-climate-change-conference-vote/")  
st.write("- https://books.openedition.org/irdeditions/23454?lang=en")  
st.write("- https://climate.nasa.gov/faq/16/is-it-too-late-to-prevent-climate-change/")  

st.markdown("-----")

