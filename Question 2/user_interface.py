from person import Person
from social_media import SocialMedia

def render_header(text):
    print()
    print("=" * 55)
    print(text.center(55))
    print("=" * 55)
    print()

def launch_interface():
    render_header("Welcome to Leong's social media application")
    input("Press 'Enter' key to proceed ...")  # waits for any key (Enter)

def main_dahsboard(socialMedia):
    # Use this as the main loop
    while True:
        render_header("Main Dashboard")
        print("1. View users")
        print("2. View connections")
        print("3. View system statistics")
        print("4. Exit")
        choice = input("\nNavigate to (1 - 6) ? : ")

        if choice == '1':
            print("Proceed to view users ...")
            all_users_interface(socialMedia)
        elif choice == '2':
            break
        elif choice == '3':
            break
        elif choice == '4':
            print("\n👋 Exiting the app ...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

def all_users_interface(socialMedia):
    while True:
        render_header("All Users")
        socialMedia.print_all_users()
        total_users = socialMedia.get_total_vertices()
        print("\nTotal users: ", total_users)
        print("Vacancies left: ", 10 - total_users)
        choice = input(f"\nView specific user (1 - {total_users}) ? : ")