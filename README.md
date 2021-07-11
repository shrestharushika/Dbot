# Sunshine
.
# DBOT- An Interactive Diabetes Prediction Bot
Diabetes is a metabolic disease that causes high blood sugar. With diabetes, your body either doesn't make enough insulin or can't effectively use the insulin it does make. It’s important to detect the diabetes in earlier stage as experts says it can be reversed only if it is detected earlier. It’s quite risky to leave the diabetes untreated. 
Our project aims to build a diabetes predicting chatbot. It will conduct a one to one text conversation with the patient using Natural Language Understanding. This personalized diabetes prediction chatbot is trained using diabetes dataset. For prediction, multiple machine learning and deep learning models are used. The consensus model using Voting Classifier an ensemble method is considered to integrate with chatbot. Patient will have interactive session with the chatbot and the answers are saved to analyze and predict whether a patient is diabetic or not.
You can view code at: [Github](https://github.com/shrestharushika/Sunshine)
## Project Abstract:
This project aims to predict whether the user has diabetes or not Using AI Chatbot. 
Researcher says that diabetes can be cure at the early stage by controlling the food habits, losing weight and following the advice of nutritionist and doctors. Leaving it untreated could result in serious health problems like heat disease that’s why it is very important to manage and controlled before it get worse by taking preventive measures. 
With this bot one can regularly check (within 6-7 weeks). It’s not possible to regularly pay a visit to doctor, it would be very expensive.  
It won’t replace doctors but this will help people to manage diabetes before it gets worse. 
This chatbot will interact just like the humans, diagnose diabetes and recommend treatments using machine learning and deep learning models.
This bot will be really helpful for diabetic patients leaving in rural areas which will suggest the patients how to control diabetes and proper diet plans. It will provide them healthcare benefits they are deprived of. 

###Market Research
Combining the knowledge of medicine and the AI mechanism results in a self-sufficient system that can be used by the masses and avoid crisis. AI bots especially chatbots are a good way to make the diabetes diagnosis and management more interactive and add the element of self introspection. Some sources state that this AI bot technology can account for around 102 billion USD in future. 
Only one research papers has been published (diabetes predicting bot), they have only used machine learning models for classification and Rasa to build AI chatbot. Rasa is a tool to build custom AI chatbots using Python and natural language understanding and is used to build complex models in a minute.
Here, we are using machine learning and deep learning both. For chatbot implementation Django web framework is used. We will use Natural Language processing to understand the text, consensus learning will be used for better prediction. 

####Technology Stack
Data pre-processing, data analysis and data splitting will be done using python packages.
For model training is done using machine learning and deep learning algorithms using python.
And chatbot is implemented using Django. For chatbot interface HTML is used and for understanding user’s text Natural Language Processing (NLP) is used. NLP engine is connected to diabetes predicting model. It will save the user’s output in pickle format. On receiving an API call, it will load the pickle file format and make available to UI using Django webserver.  
If the Chatbot predicts user is diabetic, then it will suggests some exercise and diet plan to keep it under control (Here it will act as recommendation system).

	
## Libraries used

ChatterBot            1.0.4   
chatterbot-corpus     1.2.0   
click                 8.0.1   
colorama              0.4.4   
Django                3.2.5   
pickle
mathparse             0.1.2
nltk                  3.6.2
numpy                 1.21.0
packaging             21.0
pandas                1.3.0
Pint                  0.17
pip                   19.2.3


scikit-learn          0.24.2
scipy                 1.7.0
setuptools            41.2.0
SimpleWebSocketServer 0.1.1
six                   1.16.0
sklearn               0.0
SQLAlchemy            1.2.19
sqlparse              0.4.1
threadpoolctl

## Go to path bot 
run python chatbottrain.py
run python bot_interaction.py
interact with the chatbot 
click on the form (diabetes test form)
sumit button will navigate to final prediction
