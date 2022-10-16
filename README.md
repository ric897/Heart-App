# Heart-App
Heart that help cardiac rehab and training.


## API Docs

```
[
    {
        "name": "Farrell Hardy", //Nurse Name
        "email": "nurse@email.com", //email
        "phone": "123-456-7890" //phone
        "patients": [ 
            {
                //All patients that the nurse is taking care of
                "id": 1,
                "name": "Anne Bradley",
                "email": patient@email.com,
                "phone": 123-456-7890,
                "rehab": link,
            }
        ]
            "id": 2 //nurse id 
     }
]
```


## Inspiration
It all started when I was visiting my family in Austria and I met with my aunt who was excited about her new job as head of cardiac rehab. So, I asked her about her job requirements and she went on to explain how important cardiac rehab is! So, that was the inspiration! We wanted to design an application that helps and educates therapists and patients alike who are undergoing the cardiac rehabilitation process.


## What Heart Shield Does
Key Functions of the App

### Modular Based Course Creation
- Allows therapists and caretakers to pool training and resources.
- By uploading an exercise, the caretaker makes said plan available to all other modules.
- Facilitates the creation of new plans by selecting from a pool of previously loaded exercises/activities.

### Patient Links and SMS Notifications
- Each patient gets texted their individual rehab plan and educational resources to increase patient engagement and rehab participation.
- Each patient's plan is viewable from a unique link sent in the text.

### API and Hospital Dashboard
- The implementation of an API with multiple endpoints facilitates seamless integrations and data analysis across multiple platforms.
- Allows for hospital administrations to view data across all therapists and patients

### AssemblyAI Generated Transcripts for Checkup Meetings
- Using AssemblyAI, therapists can record meeting audio and upload to HeartShield to get a transcript of the audio.
- Transcript accounts for multiple speakers and seperates dialogue between speakers


## How we built it
We built the app using Django as our main framework. However, we quickly realized that it should have cross platform compatibility so we built out a REST API.

We used the data from the API to create a quick dashboard for demoing purposes to show how valuable, not only our platform is, but also how cool our API is.


## Challenges we ran into
Definitely finding roles that fit our skill sets was difficult. Additionally, get our API to work with react was a hard issue to overcome because we had to write CORS middleware. Lastly, our REACT app crashed like 30 mins before the deadline so we had to scramble to get it up again. 


## Accomplishments that we're proud of
We were very proud of the features that we were able to implement. We were able to integrate with Twilio and AssemblyAI. Additionally, we deployed our app from a website and, all in all, had a great time!


## What We Learned
We refined and reinforced our knowledge of user-interface libraries (React), frameworks (Django), and REST APIs. The most educationally rewarding tasks proved to be connecting the Django framework back-end to the React UI front-end and learning/implementing the AssemblyAI Speech-to-Text API for transcribing patient checkups.


## What's Next for HeartShield
Redefining not only the patient but also the therapist/hospital administraton cardiac rehabilitation experience, we intend to launch a two front campaign for circulating information and raising awareness. 
- We will market to hospital administrations and promote the intrinsic benefits that Heart Shield offers in the realm of convenience and accessibilty
- We will launch a campaign to spread awareness to most at-risk populations (such as the elderly) of the benefits of cardiac rehabilition in the case of a medical emergency. Itwill be crucial that we network with Assissted Living Communities and Media COmpanies most consumed by this demographic.

As for the Heart Shield App itself, we hope to continue elevating the user experience through rolling out UI updates, whilst adding further functionality to make the experience all the more helpful and interconnected
