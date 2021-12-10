# Team Name: Sunshine
# Team Leader: Rushika Shrestha
# Team Members: Rushika Shrestha and Kanika Gupta
# Theme: HealthCare
# Hackathon: WCE 2021
# Track
Diabetes is a metabolic disease that causes high blood sugar. With diabetes, your body either doesn't make enough insulin or can't effectively use the insulin it does make. It’s important to detect the diabetes in earlier stage as experts says it can be reversed only if it is detected earlier. It’s quite risky to leave the diabetes untreated. 
Our project aims to build a diabetes predicting chatbot. It will conduct a one to one text conversation with the patient using Natural Language Understanding. This personalized diabetes prediction chatbot is trained using diabetes dataset. For prediction, multiple machine learning and deep learning models are used. The model with best accuracy score is considered to integrate with chatbot. Patient will have interactive session with the chatbot and the answers are saved to analyse and predict whether a patient is diabetic or not.


# 1.	Project Name: Dbot

# 2.	Project Abstract:
This project aims to predict whether the user has diabetes or not Using AI Chatbot. 
Researcher says that diabetes can be cure at the early stage by controlling the food habits, losing weight and following the advice of nutritionist and doctors. Leaving it untreated could result in serious health problems like heat disease that’s why it is very important to manage and controlled before it get worse by taking preventive measures. 
With this bot one can regularly check (within 6-7 weeks). It’s not possible to regularly pay a visit to doctor, it would be very expensive.  
It won’t replace doctors but this will help people to manage diabetes before it gets worse. 
This chatbot will interact just like the humans, diagnose diabetes and recommend treatments using machine learning and deep learning models.
This bot will be really helpful for diabetic patients leaving in rural areas which will suggest the patients how to control diabetes and proper diet plans. It will provide them healthcare benefits they are deprived of. 	

# 3.	Market Research
Combining the knowledge of medicine and the AI mechanism results in a self-sufficient system that can be used by the masses and avoid crisis. AI bots especially chatbots are a good way to make the diabetes diagnosis and management more interactive and add the element of self introspection. Some sources state that this AI bot technology can account for around 102 billion USD in future. 
Only one research papers has been published (diabetes predicting bot), they have only used machine learning models for classification and Rasa to build AI chatbot. Rasa is a tool to build custom AI chatbots using Python and natural language understanding and is used to build complex models in a minute.
Here, we are using machine learning and deep learning both. For chatbot implementation Django web framework is used. We will use Natural Language processing to understand the text, consensus learning will be used for better prediction. 

# 4.	Technology Stack
Data pre-processing, data analysis and data splitting will be done using python packages.
For model training is done using machine learning and deep learning algorithms using python.
And chatbot is implemented using Django. For chatbot interface HTML is used and for understanding user’s text Natural Language Processing (NLP) is used. NLP engine is connected to diabetes predicting model. It will save the user’s output in pickle format. On receiving an API call, it will load the pickle file format and make available to UI using Django webserver.  
If the Chatbot predicts user is diabetic, then it will suggests some exercise and diet plan to keep it under control (Here it will act as recommendation system).





# 5.	Innovativeness
Dbot will not only diagnose whether the user is diabetic or not but also recommend exercise and diet to control it. It is a predicting plus recommending model.
We will use consensus machine learning model to get better accuracy. 
In consensus machine learning, we will use more than one model for prediction. Suppose, out of five models  three models are giving accuracy more than 90% than we will take the probability of classification model output.
Example Two models predicted “Yes” and one model predicted “No” than final prediction will be “Yes”(Diabetic).



# 6.	Approach of Development

6.1 Data Pre-processing/Feature Selection
First of all, data pre-processing is done which includes data cleaning, data integration, data reduction and data transformation using python libraries. After data pre-processing, feature selection is done. Only features contributing to target values will be considered. 
6.2 Data Analysis
After data pre-processing, Exploratory Data Analysis is done. In this data is analysed using different charts like pie chart, bar plot, boxplot, violin plot and so on. It will help to recognize the pattern of dataset.

6.3 Data Splitting
After, dataset will be divided using train_test_split into training and testing dataset. 

6.4 Model Training and Evaluation
Then, using machine learning classification algorithms like Naïve Bayes, Decision tree, XGBoost classifier and multi-layer neural network models.  Using accuracy score and classification report models will be evaluated and the models (more than one model will be used) with highest accuracy will be linked with Chatbot.
   
 6.5 Chatbot implementation 
After model training, Chatbot is implemented using Django. It will ask few questions like user’s glucose level, body fat and blood pressure. Based on the answers given by the user ( Analysing using NLP) , if Dbot predicts that the user is diabetic then it will navigate to suggestion page which will suggest some exercises and diet plan to control the diabetes.

                      
# Flow Chart

![image](https://user-images.githubusercontent.com/46518960/145463076-33482a7d-ce12-494c-b949-4f2d976dfb7b.png)
