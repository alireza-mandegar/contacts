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


# p = Person("alireza", "09221235677", "alireza.mani95@gmail.com", "alireza_mandegar",
#            "alirezaamandegar", "alirzamandegar", "alireza-mandegar", "alirezamandegar")

con = sqlite3.connect("./contact.db")
cur = con.cursor()
# cur.execute('''CREATE TABLE contact
#                 (name, number, email, telegram, instagram, twitter, github, linkedin)''')

# def change_user


@click.command(help="to add a user to your contact")
@click.argument("name")
@click.argument("number")
@click.argument("email")
@click.argument("telegram")
@click.argument("instagram")
@click.argument("twitter")
@click.argument("github")
@click.argument("linkedin")
def add_user(name, number, email, telegram, instagram, twitter, github, linkedin):
    cur.execute(
        f"INSERT INTO contact VALUES ('{name}', '{number}', '{email}', '{telegram}', '{instagram}', '{twitter}', '{github}', '{linkedin}')")
    con.commit()


@click.command(help="to get user completely")
@click.option("--name", help="this command is based on name")
def get_user(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
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
        else:
            print("[*] not found in contact! [*]")


@click.command(help="to get user's number")
@click.option("--name", help="this command is based on name")
def get_number(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\nnumber is {p.number}")
        else:
            print("[*] not found in contact! [*]")


group.add_command(get_user)
group.add_command(add_user)
if __name__ == "__main__":
    group()
