import os
from person import Person
from social_media import SocialMedia

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_header(text):
    print()
    print("=" * 55)
    print(text.center(55))
    print("=" * 55)
    print()

def launch_interface():
    clear_screen()
    render_header("Welcome to Leong's social media application")
    input("Press 'Enter' key to proceed ...")  # waits for any key (Enter)

def main_dahsboard(socialMedia):
    clear_screen()
    # Use this as the main loop
    while True:
        render_header("Main Dashboard")
        print("1. View users")
        print("2. View connections")
        print("3. View system statistics")
        print("0. Exit")
        choice = int(input("\n👆 Navigate to? : "))

        if choice == 1:
            clear_screen()
            print("Proceed to view users ...")
            all_users_interface(socialMedia)
        elif choice == 2:
            break
        elif choice == 3:
            break
        elif choice == 0:
            clear_screen()
            print("\n👋 Exiting the app ...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

def all_users_interface(socialMedia):
    while True:
        render_header("All Users")
        print_all_users(socialMedia)
        total_users = socialMedia.get_total_vertices()
        print("\nTotal users: ", total_users)
        print(f"Vacancies left: {10 - total_users}\n")
        if total_users is 0:
            print("There is no user in this system ...\n")
        elif total_users is 10:
            print("The number of users reached the maximum capacity of this system ...\n")
        print("=" * 55)
        print()
        if total_users is 0 or total_users is 1:
            if total_users is 1:
                print(" 1.", "View specific user")
            print("11. Add new user")
            print(" 0. Back <-")
        elif total_users is 10:
            print(f"1-{total_users}.", "View specific user")
            print("  11. Add new user")
            print("   0. Back <-")
        else:
            print(f"1-{total_users}.", "View specific user")
            print(" 11. Add new user")
            print("  0. Back <-")
        choice = int(input("\n👆 Enter your choice: "))

        if choice in range (1, socialMedia.get_total_vertices() + 1):
            clear_screen()
            print_specific_user(socialMedia, choice)
            print("Navigating to all users interface ...")
        elif choice == 11:
            clear_screen()
            new_user = add_new_user()
            if new_user is not None:
                socialMedia.add_vertex(new_user)
                print(f"✅ User '{new_user.name}' is registered into the system.")
        elif choice == 0:
            clear_screen()
            print("\nBack to main dashboard ...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

def add_new_user():
    render_header("Adding New User")
    try:
        name = input("Enter name: ")
        while True:
            gender = input("Enter gender (M/F): ").strip().upper()
            if gender in ("M", "F"):
                break
            print("❗ Invalid input. Please enter 'M' - Male or 'F' - Female.")
        bio = input("Enter biography: ")

        return Person(name, gender, bio)
    
    except Exception as e:
        print(f"❗ An error occurred while adding a new user: {e}")
        return None
    
def edit_user(socialMedia, person):
    clear_screen()
    while True:
        render_header("Edit User")
        print("1. Edit name")
        print("2. Edit Biography")
        print("3. Remove a follower")
        print("4. Remove a following")
        print("0. Back <-")
        choice = int(input("\n👆 Enter your choice: "))

        if choice == 1:
            old_name = person.name
            new_name = input("Enter new name: ").strip()
            if new_name:
                person.name = new_name
                print(f"✅ Name updated from [{old_name}] to [{new_name}]!")
            else:
                print("❗ Empty new name detected. Update unsuccessful")
            break
        elif choice == 2:
            new_bio = input("Enter new biography: ").strip()
            person.biography = new_bio
            print(f"✅ {person.name}'s biography updated!")
            break
        elif choice == 3:
            clear_screen()
            while True:
                followers = get_followers(socialMedia, person)
                count = 1
                print(f"\nFollower List ({len(followers)}):")
                for follower in followers:
                    print(f"{count}. {follower}")
                    count += 1
                remove_sel = int(input("\n👆 Choose a follower to remove: "))

                if socialMedia.has_vertex(followers[remove_sel - 1]):
                    socialMedia.remove_edge(socialMedia.get_user_from_name(followers[count - 2]), person)

                # socialMedia.remove_edge(, person)
                
                break
        elif choice == 4:
            followings = get_following(socialMedia, person)
            count = 1
            print(f"\nFollowing List ({len(followings)}):")
            for following in followings:
                print(f" {count}. {following}")
                count += 1
            choice = int(input("\n👆 Choose to remove a following user: "))
            break
        elif choice == 0:
            clear_screen()
            break
        else:
            print("❗ Invalid choice. Please try again.")

def delete_user(person, socialMedia):
    while True:
        render_header("Deleting User")
        print(f"Confirm deleting this user?\n")
        print(person.show_profile())
        try:
            print()
            print("=" * 55)
            print("\n1. Delete")
            print("0. Back <-")
            choice = int(input("\n👆 Enter your choice: "))

            if choice == 1:
                clear_screen()
                socialMedia.remove_vertex(person)
                return
            elif choice == 0:
                clear_screen()
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while deleting a user: {e}")
            return None

""" Print out the list of users """
def print_all_users(socialMedia):
    count = 1
    # Loop through each person
    for vertex in socialMedia.adj_list:
        # Print the person's name 
        print(f"{count}. {vertex.name}")
        count += 1

def print_specific_user(socialMedia, id):
    person = socialMedia.get_user_from_id(id)

    while True:
        render_header(f"User Information")
        
        print(person.show_profile())

        followers = get_followers(socialMedia, person)
        print(f"\nFollower List ({len(followers)}):")
        for follower in followers:
            print(f"  - {follower}")
        
        followings = get_following(socialMedia, person)
        print(f"\nFollowing List ({len(followings)}):")
        for following in followings:
            print(f"  - {following}")
        
        print()
        print("=" * 55)
        print("\n1. Follow someone")
        print("2. Edit this user")
        print("3. Delete this user")
        print("0. Back <-")
        choice = int(input("\n👆 Enter your choice: "))

        if choice == 1:
            clear_screen()
            return
        elif choice == 2:
            clear_screen()
            print(f"Proceeding to edit user [{person.name}]")
            edit_user(socialMedia, person)
            return
        elif choice == 3:
            clear_screen()
            print(f"Proceeding to delete user [{person.name}]")
            delete_user(person, socialMedia)
            if person not in socialMedia.adj_list:
                return
        elif choice == 0:
            clear_screen()
            print("\nBack to users list ...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

def get_followers(socialMedia, person):
    return socialMedia.get_incoming_edges(person)

def get_following(socialMedia, person):
    return socialMedia.get_outgoing_edges(person)