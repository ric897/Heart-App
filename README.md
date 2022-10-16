# Heart-App
Heart that help cardiac rehab and training.


## API Example (all end points (here)[https://heartshield.io/api/])

```
[
    {
        "email": "test@heartshield.com",
        "first_name": "test",
        "start_date": "2022-10-15T05:10:39.835410Z",
        "id": 1,
        "patients": [
            {
                "id": 6,
                "name": "Alana Vernon",
                "email": "avern098@test.com",
                "phone": "4789037899",
                "link": "None",
                "supervisor": 1
            },
            {
                "id": 7,
                "name": "Issac Hayes",
                "email": "hayes890@test.com",
                "phone": "3780158930",
                "link": "None",
                "supervisor": 1
            }
            ...
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

