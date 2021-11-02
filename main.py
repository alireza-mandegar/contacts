import sqlite3
import click


@click.group()
def group():
    pass


class Person:
    def __init__(self, name, number, email, telegram, instagram, twitter, github, linkedin):
        self.name: str = name
        self.number: str = number
        self.email: str = email
        self.telegram: str = telegram
        self.instagram: str = instagram
        self.twitter: str = twitter
        self.github: str = github
        self.linkedin: str = linkedin


p = Person("alireza", "09221235677", "alireza.mani95@gmail.com", "alireza_mandegar",
           "alirezaamandegar", "alirzamandegar", "alireza-mandegar", "alirezamandegar")

con = sqlite3.connect("./contact.db")
cur = con.cursor()
cur.execute('''CREATE TABLE contact
                (name, number, email, telegram, instagram, twitter, github, linkedin)''')

# def change_user
# def add_user

@click.command(help = "to get user completely")
@click.option("--name", help = "this command is based on name")
def get_user(name, p=p):
    print(f"""
                    name is {p.name}
                    number is {p.number}
                    email is {p.email}
                    telegram is {p.telegram} and the link is https://t.me/{p.telegram}
                    instagram is {p.instagram} and the link is https://instagram.com/{p.instagram}
                    twitter is {p.twitter} and the link is https://twitter.com/{p.twitter}
                    github is {p.github} and the link is https://github.com/{p.github}
                    linkedin is {p.linkedin} and the link is https://linkedin.com/{p.linkedin}
                """)


group.add_command(get_user)
if __name__ == "__main__":
    group()
