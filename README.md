# Final Project
## Project instructions
In this open-ended assignment, you will create something that connects the astronomical concepts we have learned this semester to another discipline of interest to you.
Some possibilities include the following (although please note you are not limited to these options):

- An artistic piece (visual, performance, musical, poem, etc.) inspired by one or more topics from our course.
- A short fictional story that uses one or more concepts from our course as a plot device
- A research project about a historical person, civilization, or people group who studied the stars and used astronomical tools for aspects of their lives and work. See longer description below.
- A biographic sketch of a current astronomer who occupies one or more minoritized identities in our field. See the longer description below. Note that this assignment is not an interview!
- A researched report/explanatory video/podcast/etc. on a social issue relevant to astronomy (e.g., light pollution, Starlink satellite constellations, the racial/gender/other demographic distribution of US-based or international astronomers). 
- A series of mathematical problems (with solutions) that investigate the (astro)physics of a science fiction book/show/film using tools we have developed in this class.
- A script or program written in the programming language of your choosing in order to demonstrate a topic in astronomy, perform calculations, and plot or display the results.

Here are the **levels** of the project:
- **Level 1** projects are more limited in scope and creativity. A good Level 1 project will meet the basic criteria for the final project but may not require include novel analysis beyond presenting material from the class and external sources. Examples of past Level 1 projects have been:
Historical studies or biosketches that simply summarize information collected from external sources rather than synthesizing those sources to construct a new and interesting argument.
Software programs that calculate answers to mathematical problems using unit conversions and formulas we have frequently used in class.
Artistic pieces that may not demonstrate significant interpretive work to represent material from the class in new ways. 
I would expect a typical level 1 project to take about 5 hours to complete, and Level 1 projects will have a maximum score of 90%.

- **Level 2** projects require a greater scope and creativity. A good Level 1 project will meet the basic criteria for the final project and include novel analysis and your own interpretations beyond material from the class and external sources. Examples of past Level 2 projects have been:
Artistic pieces that demonstrate a significant attempt to express topics and ideas from the course in interesting and creative ways.
Historical research or biosketches that synthesize research from many sources to construct an interesting argument about the subject of the study and their connection to astronomy and the topics of our course.
Mathematical or computational projects that go beyond the formulas we have used in our course.
I would expect a typical Level 2 project to take about 10 hours to complete, and Level 2 projects will have a maximum score of 100%.

- **Level 3** projects meet the expectations for Level 2 projects but with higher expectations for scope, challenge, and novelty. Level 3 projects are will require significant creativity---if you are completing a project that I have mentioned as an example of a past student project, it is likely not a Level 3 project! Examples of past Level 3 projects have been:
Artistic pieces that use novel and creative methods to generate meaningful connections to our class material.
Projects that demonstrate substantial research from varied sources (e.g., primary source documents, non-online materials, living people, etc.) to generate new and interesting scholarship on an under-studied topic.
Mathematical or computational projects that require significant implementation of topics and tools beyond the scope of our course and clearly demonstrate interesting results.
Projects that make creative use of atypical formats and methods.
I would expect a typical Level 3 project to take more than 10 hours to complete. Level 3 projects will have a maximum score of 110%. This means that Level 3 projects that do not quite fulfill the proposal plan or have small deductions in other grading categories can still get a grade of 100%.

## Project Level
This is a **level 3** project.

## Background

### Notes
This story is completely fictional and is not based on any real events. 
The names of the stars are also fictional. The purpose of this story is to show how and why the encryption method could be helpful,
and why planetary values need to be encrypted. This is related to the second last unit of our course(other life in universe). 

The "Dark Forest" in the story is inspired by the book "Three Body" by Cixin Liu.

### Story

In the distant future, humans have successfully explored and colonized many planets. The two main planets are Earth and Planet Wisewave. 
The secrecy of communication between Earth and Wisdom is particularly important because both planets face a common crisis: 
alien forces are actively searching for planets with intelligent life in order to usurp resources and control the universe. 
In this universe, the "Dark Forest Law" described by Liu Cixin in "Three Bodies" is hidden, in which each civilization tries to 
find and destroy potential enemies before they are discovered and destroyed by other civilizations.

The communication between Earth and the planet Wisewave relies heavily on an interstellar encryption system. This encryption 
system uses planetary data such as mass, radius, density, semi-long axis, orbital period, orbital eccentricity, rotation period, 
and surface temperature to ensure that messages sent are not intercepted or decrypted by spies from other planets during transmission. 
This type of encryption has a high level of security because only a recipient who knows the correct planetary data and decryption 
key can decrypt the information.

Communication between Earth and the planet Wisewave includes scientific research, technological innovation, and strategic planning 
to jointly address the threat of alien invaders. By conspiring and sharing information, they attempt to reveal the intentions of 
other planets and act when necessary to protect their own survival. This interstellar encryption system provides a secure 
communication channel between the two planets, allowing them to stay in touch during the future battle for survival in the Dark Forest 
of the universe.

There is a strong cooperative relationship between Earth and Planet Wisewave, and to ensure their survival in this hostile universe, 
both planets are actively engaged in scientific research projects, studying more advanced weapons, defense systems, 
and strategies to combat alien life. They are also secretly exploring other planets in search of possible allies or additional resources.

In a universe full of dangers, the importance of interstellar encryption systems cannot be overstated. Earth and Planet Wisewave 
are constantly updating and upgrading their encryption technology to ensure that their communications are always kept at the 
highest level of security. The interstellar encryption system also allows them to share critical information quickly, 
helping them anticipate and respond to potential crises and providing strong support to survive the laws of the Dark Forest.

With the increased cooperation between Earth and Planet Wisewave, a new type of encryption algorithm has been jointly developed. 
This algorithm harnesses the immense potential of quantum computers to enhance the security of their communications to 
an unprecedented level. This allows them to gain more confidence and advantage in dealing with potential alien invaders.

### Data of the two Planet
Earth data:
```python
planet_data_dict_earth = {
    "mass": 1.0,  # Earth mass
    "radius": 6371,  # km
    "density": 5.52,  # g/cm^3
    "semi_major_axis": 1.0,  # Astronomical Units
    "orbital_period": 365.25,  # days
    "orbital_eccentricity": 0.0167,
    "rotation_period": 24.0,  # hours
    "surface_temperature": 288,  # K
}
```

The Wisewave Planet:
```python
planet_data_dict_wisewave = {
    "mass": 2.5,  # Earth mass
    "radius": 8000,  # km
    "density": 5.0,  # g/cm^3
    "semi_major_axis": 1.2,  # Astronomical Units
    "orbital_period": 430,  # days
    "orbital_eccentricity": 0.0100,
    "rotation_period": 30.0,  # hours
    "surface_temperature": 305,  # K
}
```

## How to run the code

### Requirements
- Python 3.6 or higher
- NumPy
- SciPy

### Steps
You can install the required packages by running:

```bash
pip install numpy scipy
```

Then, you can run the code by executing:

```bash
python main.py
```
This will execute the StellarEncryption class, which includes the encryption and decryption process of the planetary data and a secret message. 
You will see the encrypted vector, original message, decrypted message, original planet data, and decrypted planet data printed in the console.

Also, you can change the data in `main.py` to the planet data I provided in the story to see the result of the encryption and decryption process.