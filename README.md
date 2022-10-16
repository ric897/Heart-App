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


## What Heart Shield Does
Key Functions of the App

### Modular Based Course Creation
- Allows therapists and caretakers to pool training and resources.
- By uploading an exercise, the caretaker makes said plan available to all other modules.
- Faciliates the creation of new plans by selecting from a pool of previously loaded exercises/activities.

### Patient Links and SMS Notifications
- Each patient gets texted their individual rehab plan and educational resources to increase patient engagement and rehab participation.
- Each patient's plan is viewable from a unique link sent in the text.

### API and Hospital Dashboard
- The implementation of an API with multiple endpoints facilitates seamless integrations and data analysis across multiple platforms.
- Allows for hospital administrations to view data across all therapists and patients

### AssemblyAI Generated Transcripts for Checkup Meetings
- Using AssemblyAI, therapists can record meeting audio and upload to HeartShield to get a transcript of the audio.
- Transcript accounts for multiple speakers and seperates dialogue between speakers

