def get_user_inputs():
    print("Welcome to the Personalized Story Generator!")
    character_name = input("Enter the main character's name: ")
    setting = input("Enter the setting of the story: ")
    theme = input("Enter the theme of the story (e.g., adventure, mystery): ")
    return character_name, setting, theme