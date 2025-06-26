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
        print("1. View all users")
        print("2. View all connections")
        print("3. View system statistics")
        print("0. Exit")
        choice = int(input("\n👆 Navigate to? : "))

        if choice == 1:
            clear_screen()
            print("Proceed to view all users ...")
            all_users_interface(socialMedia)
        elif choice == 2:
            clear_screen()
            print("Proceed to view all connections ...")
            render_header("All Connections")
            print_connections(socialMedia)
            input("Press 'Enter' key to back to main dashboard ...")
            # all_users_interface(socialMedia)
        elif choice == 3:
            clear_screen()
            print("Proceed to view system statistics ...")
            render_header("System Statistics")
            print_system_stat(socialMedia)
            input("Press 'Enter' key to back to main dashboard ...")
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
        render_header(f"Edit User [{person.get_name()}]")
        print("1. Edit name")
        print("2. Edit Biography")
        print("3. Remove a follower")
        print("4. Remove a following")
        print("0. Back <-")
        choice = int(input("\n👆 Enter your choice: "))

        if choice == 1:
            old_name = person.get_name()
            new_name = input("Enter new name: ").strip()
            if new_name:
                person.set_name(new_name)
                print(f"✅ Name updated from [{old_name}] to [{new_name}]!")
            else:
                print("❗ Empty new name detected. Update unsuccessful")
        elif choice == 2:
            new_bio = input("Enter new biography: ").strip()
            person.set_bio(new_bio)
            print(f"✅ {person.get_name()}'s biography updated!")
        elif choice == 3:
            clear_screen()
            remove_follower(socialMedia, person)
        elif choice == 4:
            clear_screen()
            remove_following(socialMedia, person)
        elif choice == 0:
            clear_screen()
            break
        else:
            print("❗ Invalid choice. Please try again.")

def remove_follower(socialMedia, person):
    while True:
        render_header(f"Remove Follower For [{person.get_name()}]")
        followers = get_followers(socialMedia, person)
        count = 1
        print(f"\nFollower List ({len(followers)}):")
        for follower in followers:
            print(f"{count}. {follower}")
            count += 1
        print("\n0. Back <-")
        remove_sel = int(input("\n👆 Choose a follower to remove: "))

        if remove_sel == 0:
            clear_screen()
            break
        elif socialMedia.has_vertex(followers[remove_sel - 1]):
            try:
                socialMedia.remove_edge(socialMedia.get_vertex_from_name(followers[remove_sel - 1]), person)
                print(f"[{followers[remove_sel - 1]}] is not following [{person.get_name()}] now ...")
            except Exception as e:
                print(f"❗ An error occurred while removing a follower: {e}")
            break
        else:
            print("❗ Target user not found in the follower list. Remove follower unsuccessful ...")

def remove_following(socialMedia, person):
    while True:
        render_header(f"Remove Following For [{person.get_name()}]")
        followings = get_following(socialMedia, person)
        count = 1
        print(f"\nFollowing List ({len(followings)}):")
        for following in followings:
            print(f" {count}. {following}")
            count += 1
        print("\n0. Back <-")
        remove_sel = int(input("\n👆 Choose to remove a following user: "))
        if remove_sel == 0:
            clear_screen()
            break
        elif socialMedia.has_vertex(followings[remove_sel - 1]):
            try:
                socialMedia.remove_edge(person, socialMedia.get_vertex_from_name(followings[remove_sel - 1]))
                print(f"[{person.get_name()}] is not following [{followings[remove_sel - 1]}] now ...")
            except Exception as e:
                print(f"❗ An error occurred while removing a following user: {e}")
            break
        else:
            print("❗ Target user not found in the following list. Remove following unsuccessful ...")

def delete_user(person, socialMedia):
    while True:
        render_header(f"Deleting User [{person.get_name()}]")
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
                try:
                    socialMedia.remove_vertex(person)
                    print(f"[{person.get_name()}] profile successfully removed ...")
                    break
                except Exception as e:
                    print(f"❗ An error occurred while removing a following user: {e}")
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
    for person in socialMedia.adj_list:
        # Print the person's name 
        print(f"{count}. {person.get_name()}")
        count += 1

def print_specific_user(socialMedia, id):
    while True:
        person = socialMedia.get_vertex_from_id(id)
        try:
            render_header(f"User Information")
            
            print(person.show_profile())

            try:
                followers = get_followers(socialMedia, person)
                print(f"\nFollower List ({len(followers)}):")
                for follower in followers:
                    print(f"  - {follower}")
                
                followings = get_following(socialMedia, person)
                print(f"\nFollowing List ({len(followings)}):")
                for following in followings:
                    print(f"  - {following}")
            except Exception as e:
                continue

            print()
            print("=" * 55)
            print("\n1. Follow someone")
            print("2. Edit this user")
            print("3. Delete this user")
            print("0. Back <-")
            choice = int(input("\n👆 Enter your choice: "))

            if choice == 1:
                clear_screen()
                follow_user(socialMedia, person)
            elif choice == 2:
                clear_screen()
                print(f"Proceeding to edit user [{person.get_name()}]")
                edit_user(socialMedia, person)
            elif choice == 3:
                clear_screen()
                print(f"Proceeding to delete user [{person.get_name()}]")
                delete_user(person, socialMedia)
                if person not in socialMedia.adj_list:
                    break
            elif choice == 0:
                clear_screen()
                print("\nBack to users list ...")
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while displaying [{person.get_name()}]'s information: {e}")
            break

def follow_user(socialMedia, person):
    while True:
        count = 1
        followers = get_followers(socialMedia, person)
        combined = []

        render_header(f"Follow Someone For [{person.get_name()}]")

        for follower in followers:
            if not socialMedia.has_edge(person, socialMedia.get_vertex_from_name(follower)):
                if count == 1:
                    print(f"\nPeoples folling you that you haven't follow:")
                print(f"{count}. {follower}")
                count += 1
                combined.append(follower)

        print(f"\nRecommendations ({socialMedia.get_total_vertices() - 1 - len(followers)}):")
        for vertex in socialMedia.adj_list:
            if not socialMedia.has_edge(person, vertex) and vertex.get_name() is not person.get_name():
                # Print the person's name 
                print(f"{count}. {vertex.get_name()}")
                count += 1
                combined.append(vertex.get_name())

        try:
            print()
            print("=" * 55)
            if count == 2:
                print(f"\n1. Follow a person")
                print("0. Back <-")
            elif count > 2 and count < 10:
                print(f"\n1-{count - 1}. Follow a person")
                print("  0. Back <-")
            else:
                print("\n0. Back <-")
            choice = int(input("\n👆 Enter your choice: "))

            if count > 1 and choice in range (1, count):
                clear_screen()
                socialMedia.add_edge(person, socialMedia.get_vertex_from_name(combined[choice - 1]))
                return
            elif choice == 0:
                clear_screen()
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while following a user: {e}")
            return None

def print_connections(socialMedia):
    for person in socialMedia.adj_list:
            followers = socialMedia.get_incoming_edges(person)
            followings = socialMedia.get_outgoing_edges(person)

            max_len = max(len(followers), len(followings))

            print(f"\n* {person.get_name()}")
            print("-" * 55)
            print(f"{f'Follower ({len(followers)})':<25}Following ({len(followings)})")
            print("-" * 55)

            for i in range(max_len):
                left = followers[i] if i < len(followers) else ""
                right = followings[i] if i < len(followings) else ""
                print(f"{left:<25}{right}")
            print("-" * 55)
            print()

def print_system_stat(socialMedia):
    # To get total users
    total_users = socialMedia.get_total_vertices()

    # To get gender summary
    # To get most followers
    # To get average followers
    # To get no followers
    # To get no followings
    gender = [0, 0]
    followers_count = 0
    most_followers = 0
    no_followers = []
    no_followings = []
    no_connection = []
    for person in socialMedia.adj_list:
        if person.get_gender() == "M":
            gender[0] += 1
        elif person.get_gender() == "F":
            gender[1] += 1
        followers = socialMedia.get_incoming_edges(person)
        followings = socialMedia.get_outgoing_edges(person)
        followers_count += len(followers)

        if len(followers) > most_followers:
            most_followers = len(followers)
        
        if len(followers) == 0 and len(followings) == 0:
            no_connection.append(person.get_name())
        if len(followers) == 0:
            no_followers.append(person.get_name())
        if len(followings) == 0:
            no_followings.append(person.get_name())
            
    avg_followers = followers_count / total_users

    print(f"Total Users: {total_users}")
    print(f"Gender Overview: M ({gender[0]}) F ({gender[1]})")
    print("-" * 55)
    print(f"Average followers per user: {avg_followers}")
    print(f"User with most followers: {most_followers}")
    print(f"Users with no followers ({len(no_followers)}): {"N/A" if len(no_followers) == 0 else ", ".join(no_followers)}")
    print(f"Users not following anyone ({len(no_followings)}): {"N/A" if len(no_followings) == 0 else ", ".join(no_followings)}")
    print(f"User without connection ({len(no_connection)}): {"N/A" if len(no_connection) == 0 else ", ".join(no_connection)}")
    print("-" * 55)
    print(f"All friendships ({len(socialMedia.get_bidirectional_edges())}): {"N/A" if len(socialMedia.get_bidirectional_edges()) == 0 else ""}")
    for person1, person2 in socialMedia.get_bidirectional_edges():
        print(f"{person1.get_name()} <-> {person2.get_name()}")
    print("-" * 55)
    print()
    
def get_followers(socialMedia, person):
    return socialMedia.get_incoming_edges(person)

def get_following(socialMedia, person):
    return socialMedia.get_outgoing_edges(person)