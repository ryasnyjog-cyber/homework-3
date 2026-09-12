from random import choice


def knp():
    choices = {
        "к": "Камінь",
        "н": "Ножиці",
        "п": "Папір"
    }

    player_choice = input("Ваш вибір (к — камінь, н — ножиці, п — папір): ").lower()

    if player_choice not in choices:
        print("❌ Невірний вибір!")
        return

    computer_choice = choice(list(choices.keys()))

    print(f"\nВи обрали: {choices[player_choice]}")
    print(f"Комп'ютер обрав: {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("🤝 Нічия!")
    elif (
        (player_choice == "к" and computer_choice == "н")
        or (player_choice == "н" and computer_choice == "п")
        or (player_choice == "п" and computer_choice == "к")
    ):
        print("🎉 Перемога!")
    else:
        print("😢 Програш!")


knp()
