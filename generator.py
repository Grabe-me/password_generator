from src.services import Password, PasswordManager


def generate_new_password(source: str):
    new = Password.generate_new_password()
    p = Password(new)
    PasswordManager(source).save_password(p.password)
    return new


def save_your_password(source: str, password: str):
    p = Password(password)
    PasswordManager(source).save_password(p.password)
    return p.password


def show_saved_password(source: str):
    if s := PasswordManager(source).read_password():
        p = Password(s, reverse=True)
        return p.password


def available_sources():
    if sources := PasswordManager.get_saved_sources():
        sources_to_str = "\n\t".join(sources)
        return f"Saved SOURCES: {sources_to_str}"


def main():
    while True:
        sources = None

        flag = input(
            "--g to generate new password\n"
            "--p to save your own password\n"
            "--s to show your saved password\n\n"
            "--q to Exit\n\n"
            ">>> "
        )

        if flag == "--q":
            break
        elif flag not in ["--g", "--p", "--s"]:
            continue
        elif flag == "--s":
            sources = available_sources()
            if not sources:
                print("There is No any saved Sources\n")

                continue

        source = input(
            "Enter SOURCE which you prefer (example: GitHib)\n\n"
            ">>> "
        )

        match flag:
            case "--g":
                pwd = generate_new_password(source)
                print(pwd)
            case "--p":
                pwd = input("Enter YOUR password\n\n>>> ")
                save_your_password(source, pwd)
            case "--s":
                pwd = show_saved_password(source) or sources
                print(pwd)


if __name__ == "__main__":
    main()