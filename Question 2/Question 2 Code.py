import random
from person import Person
from social_media import SocialMedia
import user_interface

def main():

    socialMedia = SocialMedia()
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

    # Add all users to the graph
    for user in users:
        socialMedia.add_vertex(user)

    # Randomly assign followings (edges)
    for user in users:
        # Choose a random number of people to follow (1 to 3 others)
        num_to_follow = random.randint(1, 3)
        # Choose targets excluding self
        possible_targets = [u for u in users if u != user]
        to_follow = random.sample(possible_targets, k=num_to_follow)
        
        for target in to_follow:
            socialMedia.add_edge(user, target)

    print("\n=== Summary ===")
    for person in users:
        followers = socialMedia.get_incoming_edges(person)
        followings = socialMedia.get_outgoing_edges(person)
        print(f"\n{person.name}")
        print(f"  Followers  ({len(followers)}): {followers}")
        print(f"  Following  ({len(followings)}): {followings}")

    user_interface.launch_interface()

    user_interface.main_dahsboard(socialMedia)

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()