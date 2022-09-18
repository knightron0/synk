# synk.
Learning is not always easy, and the giant lecture halls, coughing students, and monotonous content may make it difficult to pay attention during lectures. A study conducted by MIT shows that the large majority of students only attend half of the lectures they have.

That’s why many students resort to using online lecture videos, but due to being completely disconnected from a live experience, they lose out on many key learning points.

This is where Synk comes into play. It combines the online learning experience and the in-person learning experience, synchronizing them together. Research has shown that group studying is more effective, so Synk tries to implement this. Our website allows lecture videos to be played together with others through room links, enabling chatting to understand the content better. Synk also automatically sources through the video to display the most important content at different timestamps and provides a transcript for those who have trouble hearing lectures in person.

Synk also acts as a forum app. Users upload lecture videos for moderators to review and then appears on the homepage under specific class sections. Each lecture also has a comment section, which keeps track of where in the video the user has commented. For example, while I am watching Professor Chen’s ingenious teaching on calculus 3, I get 15 minutes in, on partial derivatives. I’m not quite sure professor Chen derived that twice! I’ll just leave a comment, and hope someone can answer it. The comment is then lodged along with the video timestamp of 15 minutes, so someone else can go through to that time to gain some context and answer my question.

We built the frontend of Synk using HTML, CSS, and Javascript. We used bootstrap 4 CSS as our element framework, and created files for each individual page for navigation. The backend was primarily implemented using Flask and Socket.IO in Python. To generate the keywords and transcription of the lecture, we used DeepSpeech and YAKE!, which are state-of-the-art natural language processing pretrained models implemented in Python. We used Firebase as a real-time database and manipulated it using JavaScript.

We hope that Synk can synchronize the learning of students and simplify the process of education. As we continue to develop Synk, we hope more and more students will discover the possibilities of Synk and create a large community for everyone to benefit. This is Synk. Synchronizing education.

Sources: https://web.mit.edu/fnl/volume/184/breslow.html, https://www.studyusa.com/en/a/1980/better-to-study-alone-or-in-a-group


Video link: https://youtu.be/ZVjPCn8sJjE
