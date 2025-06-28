import random
from person import Person
from social_media import SocialMedia
import user_interface

# =============================================================================
#                        MAIN PROGRAM EXECUTION FLOW
# =============================================================================

def main():
    # Create social media instance
    socialMedia = SocialMedia()
    # Add dummy users into social media app
    users = [
        Person('Leong Zi Qi', 'M', 'Just a banana enthusiast 🍌', False,),
        Person('Pey Hui Yi', 'F', 'Bookworm and nature lover 📚🌿', True),
        Person('Tan Zhi Qi', 'F', 'Runner, coder, dreamer 🏃‍♀️💻', True),
        Person('Jason Wong', 'M', 'Coffee is life ☕', False),
        Person('Amira Afiqah', 'F', 'Graphic designer & cat person 🐱🎨', False),
        Person('Aaron Lim', 'M', 'Love solving puzzles and writing code 🧩👨‍💻', True),
        Person('Nur Sarah', 'F', 'Baking & K-drama bingeing 🍰📺', True),
        Person('Marcus Tan', 'M', 'Climbing mountains one app at a time ⛰️📱', False),
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