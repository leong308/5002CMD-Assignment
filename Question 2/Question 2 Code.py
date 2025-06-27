import random
from person import Person
from social_media import SocialMedia
import user_interface

def main():
    # Create social media instance
    socialMedia = SocialMedia()
    # Add dummy users into social media app
    users = [
        Person('Leong Zi Qi', 'M', 'Just a banana enthusiast 🍌'),
        Person('Pey Hui Yi', 'F', 'Bookworm and nature lover 📚🌿'),
        Person('Tan Zhi Qi', 'F', 'Runner, coder, dreamer 🏃‍♀️💻'),
        Person('Jason Wong', 'M', 'Coffee is life ☕'),
        Person('Amira Afiqah', 'F', 'Graphic designer & cat person 🐱🎨'),
        Person('Aaron Lim', 'M', 'Love solving puzzles and writing code 🧩👨‍💻'),
        Person('Nur Sarah', 'F', 'Baking & K-drama bingeing 🍰📺'),
        Person('Marcus Tan', 'M', 'Climbing mountains one app at a time ⛰️📱'),
    ]

    # Add all users into social media
    for user in users:
        socialMedia.add_vertex(user)

    # Randomly assign followings
    for user in users:
        # Choose a random number of people to follow
        num_to_follow = random.randint(1, 4)
        # Choose targets excluding self
        possible_targets = [u for u in users if u != user]
        to_follow = random.sample(possible_targets, k = num_to_follow)
        for target in to_follow:
            socialMedia.add_edge(user, target)

    # Main program execution
    user_interface.launch_interface(socialMedia)

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()