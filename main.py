import file_operations
import os
from faker.generator import random
from faker import Faker


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]

ALPHABET = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def runic_skills_generator(SKILLS, ALPHABET):
    runic_skills = []
    for skill in SKILLS:
        for letter, styled_letter in ALPHABET.items():
            skill = skill.replace(letter, styled_letter)
        runic_skills.append(skill)
    return runic_skills


def main():

    fake = Faker("ru_RU")
    os.makedirs("output", mode=0o777, exist_ok=True)

    for output in range(10):

        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()

        strength = random.randrange(3, 17)
        agility = random.randrange(3, 17)
        endurance = random.randrange(3, 17)
        intelligence = random.randrange(3, 17)
        luck = random.randrange(3, 17)

        runic_skills = runic_skills_generator(SKILLS, ALPHABET)
        skills_list = random.sample(runic_skills, 3)

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "skill_1": skills_list[0],
            "skill_2": skills_list[1],
            "skill_3": skills_list[2]
        }

        file_operations.render_template("charsheet.svg", f"output/{first_name}_{last_name}.svg", context)


if __name__ == '__main__':
    main()
