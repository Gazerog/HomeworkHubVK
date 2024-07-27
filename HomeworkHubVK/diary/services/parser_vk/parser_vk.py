import os

from HomeworkHubVK.HomeworkHubVK.diary.models import Homework
from main import main

password = str(os.getenv('password_of_vk'))
mail = str(os.getenv("mail"))


def parse_all_vk_posts(names_discipline: list[str], mail_of_vk=mail, password_of_vk=password):
    all_posts = main(names_discipline=names_discipline, mail_of_vk=mail_of_vk, password_of_vk=password_of_vk)
    Homework.objects.update_of_create()
