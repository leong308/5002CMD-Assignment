from person import Person
from social_media import SocialMedia
import user_interface

def main():

    socialMedia = SocialMedia()
    person1 = Person('Leong Zi Qi', 'Male', '', False)
    person2 = Person('Pey Hui Yi', 'Female', '', False)
    person3 = Person('Tan Zhi Qi', 'Female', '', False)

    socialMedia.addVertex(person1)
    socialMedia.addVertex(person2)
    socialMedia.addVertex(person3)

    socialMedia.add_edge(person1, person2)
    socialMedia.add_edge(person1, person3)
    socialMedia.add_edge(person2, person1)
    # socialMedia.remove_edge(person1, person2)

    print("Has Edge? ",socialMedia.has_edge(person1, person2))

    socialMedia.print_adj_list()
    print(socialMedia.has_vertex('Pey Hui Yi'))
    socialMedia.remove_vertex(person2)
    print(socialMedia.has_vertex('Pey Hui Yi'))
    print("Has Edge? ",socialMedia.has_edge(person1, person2))

    socialMedia.print_adj_list()
    user_interface.launch_interface()

    user_interface.main_dahsboard(socialMedia)

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()