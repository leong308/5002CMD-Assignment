import os                   # Import this for clear screen purpose
from person import Person   # Import this for add user purpose

##################################################################################################################################
""" Cleanup the current terminal's display """
##################################################################################################################################
def clear_screen():
    # cls is for Windows (nt)
    # clear is for macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

##################################################################################################################################
""" Render the header with predefined UI design """
##################################################################################################################################
def render_header(text):
    print()
    print("=" * 55)
    print(text.center(55))      # Center the header title
    print("=" * 55)
    print()

##################################################################################################################################
""" Main interface of the program (one-time) """
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def launch_interface(socialMedia):
    clear_screen()
    render_header("Welcome to Leong's social media application")
    input("Press 'Enter' key to proceed ...")       # Waits for enter key to proceed
    main_dahsboard(socialMedia)

##################################################################################################################################
""" Main loop (dashboard) of the program """
"""
    This dashboard alllows users to:
    - select to view all users within the system
    - select to view all connections between every users
    - select to view comprehensive statistics of the system
    - select to exit the program
"""
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def main_dahsboard(socialMedia):
    clear_screen()
    # Use this as the main loop
    while True:
        render_header("Main Dashboard")
        print("1. View all users")
        print("2. View all connections")
        print("3. View system statistics")
        print("0. Exit")
        choice = input("\n👆 Navigate to? : ")
        # Prevent ValueError exceptions
        if choice.isdigit():
            choice = int(choice)
        
        # When user selected to view all users
        if choice == 1:
            clear_screen()
            print("Proceed to view all users ...")
            all_users_interface(socialMedia)
        # When user selected to view all connections
        elif choice == 2:
            clear_screen()
            print("Proceed to view all connections ...")
            render_header("All Connections")
            print_connections(socialMedia)
            input("Press 'Enter' key to back to main dashboard ...")    # Waits for enter key to proceed
        # When user selected to view system statistics
        elif choice == 3:
            clear_screen()
            print("Proceed to view system statistics ...")
            render_header("System Statistics")
            print_system_stat(socialMedia)
            input("Press 'Enter' key to back to main dashboard ...")    # Waits for enter key to proceed
        # When user selected to exit the program
        elif choice == 0:
            clear_screen()
            print("\n👋 Exiting the app ...")
            break
        # When entered choices are invalid
        else:
            print("❗ Invalid choice. Please try again.")

##################################################################################################################################
""" To display all users at a glance """
"""
    This interface alllows users to:
    - view a list of all users within the system
    - view total users count and vacancies left
    - select to view a specific user in the system
    - select to add a new user into the system
    - select to back to main dashboard
"""
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def all_users_interface(socialMedia):
    # Loop until user wish to back to main dashboard
    while True:
        render_header("All Users")
        total_users = socialMedia.get_total_vertices()  # Fetch total users
        # Only prints if there are users exists
        if total_users > 0:
            print_all_users(socialMedia)
        else:
            print("There is no user in this system ...\n")
        print("\nTotal users: ", total_users)           # Print total existing users
        print(f"Vacancies left: {10 - total_users}\n")  # Print vacancies left for adding users

        if total_users == 10:
            print("The number of users reached the maximum capacity of this system ...\n")
        print("=" * 55)
        print()

        # Logics to beautify UI
        if total_users == 0 or total_users == 1:
            if total_users == 1:
                print(" 1.", "View specific user")
            print("11. Add new user")
            print(" 0. Back <-")
        elif total_users == 10:
            print(f"1-{total_users}.", "View specific user")
            print("   0. Back <-")
        else:
            print(f"1-{total_users}.", "View specific user")
            print(" 11. Add new user")
            print("  0. Back <-")
        choice = input("\n👆 Enter your choice: ")
        # Prevent ValueError exceptions
        if choice.isdigit():
            choice = int(choice)

        # When user selected to view a specific user
        # Check if the choice is in range of the total users
        # Check whether there is at least 1 user in the system
        if choice in range (1, socialMedia.get_total_vertices() + 1) and total_users > 0:
            clear_screen()
            print_specific_user(socialMedia, choice)
            print("Navigating to all users interface ...")
        # When user selected to add new user
        # Check whether the total users is less than 10 now
        elif choice == 11 and total_users < 10:
            clear_screen()
            new_user = add_new_user()
            # If user is successfully created
            if new_user is not None:
                # Add person into socialMedia
                socialMedia.add_vertex(new_user)
                print(f"✅ User '{new_user.name}' is registered into the system.")
        # When user selected to back to main dashboard
        elif choice == 0:
            # Navigate back to main dashboard
            clear_screen()
            print("\nBack to main dashboard ...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

##################################################################################################################################
""" To add a new person """
"""
    This interface alllows users to:
    - enters new person's name
    - enters new person's gender in M or F
    - enters new person's biography (optional)
"""
""" Return: New person's object (class) """
##################################################################################################################################
def add_new_user():
    render_header("Adding New User")
    try:
        # Loop until user enters a valid name
        while True:
            name = input("Enter name: ").strip()
            # Ends the loop if name is not empty
            if len(name) > 0:
                break
            else:
                print("❗ Invalid input. Please enter a valid profile name.\n")
        # Loop until user enters a valid gender
        while True:
            gender = input("Enter gender (M/F): ").strip().upper()
            if gender in ("M", "F"):
                break
            print("❗ Invalid input. Please enter 'M' - Male or 'F' - Female.\n")
        # Biography is optional, accepts any form of input
        bio = input("Enter biography: ").strip()
        # Loop until user enters a valid privacy type
        while True:
            private = input("Make it a private account (Y/N): ").strip().upper()
            if private in ("Y", "N"):
                break
            print("❗ Invalid input. Please enter 'Y' - Set as Private Account or 'F' - Set as Public Account .\n")

        # Create and return new person's object
        return Person(name, gender, bio, True if private == "Y" else False)
    
    except Exception as e:
        print(f"❗ An error occurred while adding a new user: {e}")
        return None
    
##################################################################################################################################
""" To edit the person """
"""
    This interface alllows users to:
    - select to edit person's name
    - select to edit person's biography
    - select to remove the person's follower
    - select to remove the person's following
    - select to back to specific user page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
##################################################################################################################################
def edit_user(socialMedia, person):
    clear_screen()
    # Loop until user wish to back to specific user interface
    while True:
        render_header(f"Edit User [{person.get_name()}]")
        print("1. Edit name")
        print("2. Edit Biography")
        print("3. Edit Privacy")
        print("4. Remove a follower")
        print("5. Remove a following")
        print("0. Back <-")
        choice = input("\n👆 Enter your choice: ")
        # Prevent ValueError exceptions
        if choice.isdigit():
            choice = int(choice)

        # When user selected to edit name
        if choice == 1:
            old_name = person.get_name()
            new_name = ""
            # Loop until user enters a valid new name
            while True:
                new_name = input("Enter name: ").strip()
                # Ends the loop if name is not empty
                if len(new_name) > 0:
                    person.set_name(new_name)
                    print(f"✅ Name updated from [{old_name}] to [{new_name}]!")
                    break
                else:
                    print("❗ Invalid input. Please enter a valid new profile name.\n")
        # When user selected to edit biography
        elif choice == 2:
            new_bio = input("Enter new biography: ").strip()
            person.set_bio(new_bio)
            print(f"✅ {person.get_name()}'s biography updated!")
        # When user selected to edit privacy
        elif choice == 3:
            # Loop until user wish to back to edit user interface
            while True:
                # Display the account type
                print(f"\nCurrent account type: {"Private" if person.get_privacy() else "Public"}")
                selection = input("Enter 1 to toggle privacy or 0 to abort operation: ")
                # Prevent ValueError exceptions
                if selection.isdigit():
                    selection = int(selection)

                # When user selected to toggle the person's privacy
                if selection == 1:
                    # Perform toggle privacy action
                    person.set_privacy(not person.get_privacy())
                    print(f"✅ {person.get_name()}'s privacy updated!")
                    break
                # When user selected to abort and back to edit user page
                elif selection == 0:
                    clear_screen()
                    break
                else:
                    print("❗ Invalid selection. Please try again.")
        # When user selected to remove a follower
        elif choice == 4:
            # Check if there is any follower available to remove
            if len(get_followers(socialMedia, person)) > 0:
                clear_screen()
                remove_follower(socialMedia, person)
            else:
                print("This user have no follower to remove ...")
        # When user selected to remove a following
        elif choice == 5:
            # Check if there is any following available to remove
            if len(get_following(socialMedia, person)) > 0:
                clear_screen()
                remove_following(socialMedia, person)
            else:
                print("This user have no following to remove ...")
        # When user selected to back to edit user page
        elif choice == 0:
            clear_screen()
            break
        else:
            print("❗ Invalid choice. Please try again.")

##################################################################################################################################
""" To remove a follower """
"""
    This interface alllows users to:
    - view all of the user's followers list
    - select to remove follower from the list
    - select to back to edit user page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
##################################################################################################################################
def remove_follower(socialMedia, person):
    # Loop until user wish to cancel deletion and back to edit user interface
    while True:
        render_header(f"Remove Follower For [{person.get_name()}]")
        followers = get_followers(socialMedia, person)      # Fetch all followers for this person
        count = 1   # For UI
        print(f"Follower List ({len(followers)}):")
        for follower in followers:
            print(f"{count}. {follower}")
            count += 1
        print("\n0. Back <-")
        remove_sel = input("\n👆 Choose a follower to remove: ")
        # Prevent ValueError exceptions
        if remove_sel.isdigit():
            remove_sel = int(remove_sel)

        # When user selected to back to edit user page
        if remove_sel == 0:
            clear_screen()
            break
        # When user selected to remove follower from list
        # Check whether the user exists
        elif remove_sel in range (count) and socialMedia.has_vertex(followers[remove_sel - 1]):
            try:
                # Perform remove follower action
                socialMedia.remove_edge(socialMedia.get_vertex_from_name(followers[remove_sel - 1]), person)
                print(f"[{followers[remove_sel - 1]}] is not following [{person.get_name()}] now ...")
            except Exception as e:
                print(f"❗ An error occurred while removing a follower: {e}")
            break
        else:
            print("❗ Target user not found in the follower list. Remove follower unsuccessful ...")

##################################################################################################################################
""" To remove a user from following """
"""
    This interface alllows users to:
    - view all of the user's following list
    - select to remove a user from the following list
    - select to back to edit user page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
##################################################################################################################################
def remove_following(socialMedia, person):
    # Loop until user wish to cancel deletion and back to edit user interface
    while True:
        render_header(f"Remove Following For [{person.get_name()}]")
        followings = get_following(socialMedia, person)     # Fetch all followings for this person
        count = 1   # For UI
        print(f"Following List ({len(followings)}):")
        for following in followings:
            print(f" {count}. {following}")
            count += 1
        print("\n0. Back <-")
        remove_sel = input("\n👆 Choose to remove a following user: ")
        # Prevent ValueError exceptions
        if remove_sel.isdigit():
            remove_sel = int(remove_sel)

        # When user selected to back to edit user page
        if remove_sel == 0:
            clear_screen()
            break
        # When user selected to remove user from following list
        # Check whether the user exists
        elif remove_sel in range (count) and socialMedia.has_vertex(followings[remove_sel - 1]):
            try:
                # Perform remove following action
                socialMedia.remove_edge(person, socialMedia.get_vertex_from_name(followings[remove_sel - 1]))
                print(f"[{person.get_name()}] is not following [{followings[remove_sel - 1]}] now ...")
            except Exception as e:
                print(f"❗ An error occurred while removing a following user: {e}")
            break
        else:
            print("❗ Target user not found in the following list. Remove following unsuccessful ...")

##################################################################################################################################
""" To delete a user from the system """
"""
    This interface alllows users to:
    - view all of the user's information
    - select to confirm to delete the person
    - select to back to specific user page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
##################################################################################################################################
def delete_user(socialMedia, person):
    # Loop until user wish to cancel deletion and back to specific user interface
    while True:
        render_header(f"Deleting User [{person.get_name()}]")
        print(f"Confirm deleting this user?\n")
        print(person.show_profile())
        try:
            print()
            print("=" * 55)
            print("\n1. Delete")
            print("0. Back <-")
            choice = input("\n👆 Enter your choice: ")
            # Prevent ValueError exceptions
            if choice.isdigit():
                choice = int(choice)

            # When user selected to delete user
            if choice == 1:
                clear_screen()
                try:
                    # Perform delete action
                    socialMedia.remove_vertex(person)
                    print(f"[{person.get_name()}] profile successfully removed ...")
                    break
                except Exception as e:
                    print(f"❗ An error occurred while removing a following user: {e}")
            # When user selected to back to specific user page
            elif choice == 0:
                clear_screen()
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while deleting a user: {e}")
            return None

##################################################################################################################################
""" To follow other users """
"""
    This interface alllows users to:
    - view all of the self unfollowed followers list
    - view all of the recommendations
    - select to follow a person from the lists
    - select to back to specific user page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
##################################################################################################################################
def follow_user(socialMedia, person):
    # Loop until user wish to back to specific user interface
    while True:
        count = 1   # For UI
        followers = get_followers(socialMedia, person)  # Fetch all followers for this person
        followings = get_following(socialMedia, person) # Fetch all followings for this person
        combined = []                                   # List to combine followers & recommendations

        render_header(f"Follow Someone For [{person.get_name()}]")
        try:
            # Loop through each follower
            for follower in followers:
                # Check if the current user doesn't follow back the follower
                if not socialMedia.has_edge(person, socialMedia.get_vertex_from_name(follower)):
                    # Print title for first instance only
                    if count == 1:
                        print(f"\nPeoples folling you that you haven't follow:")
                    print(f"{count}. {follower}")
                    count += 1                  # Increment count
                    combined.append(follower)   # Append the unfollowed follower into the combined list
        except Exception as e:
            print(f"❗ An error occurred while rendering non-following followers for [{person.get_name()}]: {e}")

        try:
            # Recommendations includes those who are not following the person and followed by the person
            # Exclude the count (friend suggestion) to prevent duplicate display below
            print(f"\nRecommendations ({socialMedia.get_total_vertices() - count - len(followings)}):")
            # Loop through each vertex
            for vertex in socialMedia.adj_list:
                # Check if the current user is not following the vertex (another person)
                # Check to prevent following ownself
                if not socialMedia.has_edge(person, vertex) and vertex.get_name() is not person.get_name():
                    # Check if the vertex (another person) is not following the user (prevent duplicate)
                    if not socialMedia.has_edge(vertex, person):
                        # Print the vertex's (another person) name 
                        print(f"{count}. {vertex.get_name()}")
                        count += 1                          # Increment count
                        combined.append(vertex.get_name())  # Append the recommendation into the combined list
        except Exception as e:
            print(f"❗ An error occurred while rendering follow recommendations for [{person.get_name()}]: {e}")

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
            choice = input("\n👆 Enter your choice: ")
            # Prevent ValueError exceptions
            if choice.isdigit():
                choice = int(choice)

            # When user selected to follow someone
            # Check if there is at least 1 available user to follow (count = 2 onwards)
            if count > 1 and choice in range (1, count):
                clear_screen()
                try:
                    # Perform follow action
                    socialMedia.add_edge(person, socialMedia.get_vertex_from_name(combined[choice - 1]))
                except Exception as e:
                    print(f"❗ An error occurred while adding connection [{person.get_name()}] --> [{combined[choice - 1]}]: {e}")
                return
            # When user selected to back to specific user page
            elif choice == 0:
                clear_screen()
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while following a user: {e}")
            return None

##################################################################################################################################
""" Print out the list of all users """
"""
    This interface alllows users to:
    - view all of the user's information
    - view followers and follwoings list
    - select to follow someone within the system
    - select to edit the current user
    - select to delete the current user
    - select to back to all users page
"""
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: id count (int) """
##################################################################################################################################
def print_specific_user(socialMedia, id):
    # Loop until user wish to back to all users interface
    while True:
        # Fetch the person's object from the id count
        # Not fetching person before calling this function 
        # because there may be updates afterwards
        # Need to fetch everytime it re-loops
        person = socialMedia.get_vertex_from_id(id)
        try:
            render_header(f"User Information")
            print(person.show_profile())
            
            followers = get_followers(socialMedia, person)      # Fetch all followers for this person
            followings = get_following(socialMedia, person)     # Fetch all followings for this person

            # When the private status if False
            # Display followers and followings
            if not person.get_privacy():
                print(f"\nFollower List ({len(followers)}):")
                for follower in followers:
                    print(f"  - {follower}")
                print(f"\nFollowing List ({len(followings)}):")
                for following in followings:
                    print(f"  - {following}")
            print()
            print("=" * 55)
            print("\n1. Follow someone")
            print("2. Edit this user")
            print("3. Delete this user")
            print("0. Back <-")
            choice = input("\n👆 Enter your choice: ").strip()
            # Prevent ValueError exceptions
            if choice.isdigit():
                choice = int(choice)

            # When user selected to follow someone
            if choice == 1:
                # If total followings count is equal to all other users in the system
                # Prevent user to proceed
                if len(followings) == socialMedia.get_total_vertices() - 1:     # Excluding itself
                    print("This user had followed all users ...")
                else:
                    clear_screen()
                    print(f"Proceeding to follow users page ...")
                    follow_user(socialMedia, person)
            # When user selected to edit the current user
            elif choice == 2:
                clear_screen()
                print(f"Proceeding to edit user [{person.get_name()}] ...")
                edit_user(socialMedia, person)
            # When user selected to delete the current user
            elif choice == 3:
                clear_screen()
                print(f"Proceeding to delete user [{person.get_name()}] ...")
                delete_user(socialMedia, person)
                # When this user is successfully deleted
                # Prompt user back to all users list (since the current user is not available now)
                if person not in socialMedia.adj_list:
                    break
            # When user selected to back to all users interface
            elif choice == 0:
                clear_screen()
                print("\nBack to all users list ...")
                break
            else:
                print("❗ Invalid choice. Please try again.")
        except Exception as e:
            print(f"❗ An error occurred while displaying [{person.get_name()}]'s information: {e}")
            break

##################################################################################################################################
""" Print out the list of all users """
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def print_all_users(socialMedia):
    count = 1   # For UI
    # Loop through each person
    try:
        for person in socialMedia.adj_list:
            # Print the person's name in format (1. Name)
            print(f"{count}. {person.get_name()}")
            count += 1  # Increment count
    except Exception as e:
        print(f"❗ An error occurred while printing all users: {e}")

##################################################################################################################################
""" To print all connections between every users in a table format """
"""
    * Name
    -------------------------------------------------------
    Follower (1)             Following (2)
    -------------------------------------------------------
    xxx                      yyy
                             zzz
    -------------------------------------------------------
"""
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def print_connections(socialMedia):
    try:
        # Loop through each person's key (object)
        for person in socialMedia.adj_list:
            followers = get_followers(socialMedia, person)      # Fetch all followers for this person
            followings = get_following(socialMedia, person)     # Fetch all followings for this person

            max_len = max(len(followers), len(followings))      # Calculate the maximum count of followers/followings for UI

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
    except Exception as e:
        print(f"❗ An error occurred while printing all user's connections: {e}")

##################################################################################################################################
""" To display all system's statistics """
"""
    This interface alllows users to:
    - view total users count
    - view gender overview/summary
    - view average followers per user
    - view users with most followers
    - view users with no follower
    - view users with not following anyone
    - view users without connection
    - view all friendships (following each other)
"""
""" Parameter: socialMedia object (class) """
##################################################################################################################################
def print_system_stat(socialMedia):
    total_users = socialMedia.get_total_vertices()  # fetch total users count
    gender = [0, 0]                                 # To get gender summary (Male, Female)
    private = 0                                     # To get the total of private accounts
    followers_count = 0                             # To get followers count
    most_followers = ['', 0]                        # To get most followers
    most_followings = ['', 0]                       # To get most followings
    no_followers = []                               # To get names of no followers
    no_followings = []                              # To get names of no followings
    no_connection = []                              # To get names of no followers and no followings

    # Loop through each person's key (object)
    for person in socialMedia.adj_list:
        if person.get_gender() == "M":
            gender[0] += 1      # If the person's gender is male (M)
        elif person.get_gender() == "F":
            gender[1] += 1      # If the person's gender is female (F)
        
        if person.get_privacy():
            private += 1        # If the person's privacy is set to True

        followers = get_followers(socialMedia, person)      # Fetch all followers for this person
        followings = get_following(socialMedia, person)     # Fetch all followings for this person
        followers_count += len(followers)                   # Get the followers count for this person

        # Check if this person's followers is bigger than the current most
        if len(followers) > most_followers[1]:
            most_followers[0] = person.get_name()   # Update new person into most_followers[0]
            most_followers[1] = len(followers)      # Update new value  into most_followers[1]
        
        # Check if this person's followings is bigger than the current most
        if len(followings) > most_followings[1]:
            most_followings[0] = person.get_name()   # Update new person into most_followings[0]
            most_followings[1] = len(followings)      # Update new value  into most_followings[1]
        
        # Check if this person has no connection with others
        if len(followers) == 0 and len(followings) == 0:
            no_connection.append(person.get_name())
        # Check if this person has no followers
        if len(followers) == 0:
            no_followers.append(person.get_name())
        # Check if this person is not following the others
        if len(followings) == 0:
            no_followings.append(person.get_name())
            
    avg_followers = followers_count / total_users           # Calculate average followers per user
    friendships = socialMedia.get_bidirectional_edges()     # Fetch all of the friendships

    print(f"Total Users: {total_users}")
    print(f"Gender Overview: M ({gender[0]}) F ({gender[1]})")
    print(f"Total Private Accounts: {private}")
    print("-" * 55)
    print(f"Average Followers Per User: {avg_followers}")
    print(f"User With Most Followers: {most_followers[0]} ({most_followers[1]})")
    print(f"User With Most Followings: {most_followings[0]} ({most_followings[1]})")
    print(f"Users With No Follower ({len(no_followers)}): {"N/A" if len(no_followers) == 0 else ", ".join(no_followers)}")
    print(f"Users Not Following Anyone ({len(no_followings)}): {"N/A" if len(no_followings) == 0 else ", ".join(no_followings)}")
    print(f"User Without Connection ({len(no_connection)}): {"N/A" if len(no_connection) == 0 else ", ".join(no_connection)}")
    print("-" * 55)
    print(f"All Friendships ({len(friendships)}): {"N/A" if len(friendships) == 0 else ""}")
    for person1, person2 in friendships:
        print(f"{person1.get_name()} <-> {person2.get_name()}")
    print("-" * 55)
    print()

##################################################################################################################################
""" Fetch all followers for a person """
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
""" Return: All followers (list) """
##################################################################################################################################
def get_followers(socialMedia, person):
    return socialMedia.get_incoming_edges(person)

##################################################################################################################################
""" Fetch all followings of a person """
""" Parameter 1: socialMedia object (class) """
""" Parameter 2: person object (class) """
""" Return: All followings (list) """
##################################################################################################################################
def get_following(socialMedia, person):
    return socialMedia.get_outgoing_edges(person)