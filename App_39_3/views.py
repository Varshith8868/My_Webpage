from django.shortcuts import render

def profile(request):
    context = {
        'name': 'NAME: Konala Varshith Pramodh Sri Sai',
        'bio': """I am a dedicated B-Tech student specializing in Artificial Intelligence and Data Science at KL University, Hyderabad.
                  With a passion for leveraging technology to solve real-world problems,
                  I’m committed to building a strong foundation in AI, machine learning, and data visualization.

        Education: Currently pursuing a B-Tech in Artificial Intelligence and Data Science at KL University, Hyderabad (2nd Year).

Technical Skills: Proficient in C, Java, and Python Full Stack Development.

Projects: 
- **Music Player**: Developed a user-friendly music player in Django, leveraging SQLite for database management.
- **MediPredict**: Created a health analytics project aimed at predictive analysis and user-friendly visualizations.

Achievements:
- Successfully completed several data analysis projects, honing skills in extracting actionable insights.
- Recognized for contributions to team projects in both coursework and extracurricular activities.

Personal Development Goals: Focused on advancing data visualization techniques to uncover deeper insights from data.

Hobbies and Interests: Passionate about cricket, and actively interested in MMA and boxing.

Strengths and Values: Known for adaptability, discipline, and a strong commitment to continuous improvement in both personal and professional pursuits.

Languages: Fluent in English, Telugu, and Hindi.

Aspirations: Dedicated to becoming an expert in AI, machine learning, and data visualization, with a long-term goal of contributing to innovative solutions in technology.""",
        'profile_pic_url': 'images/profile.jpg',  # Ensure the image is saved in static/images folder
    }
    return render(request, 'profile.html', context)
