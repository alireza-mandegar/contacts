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


@click.command(help="to get user's email")
@click.option("--name", help="this command is based on name")
def get_email(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\nemail is {p.email}")
        else:
            print("[*] not found in contact! [*]")

@click.command(help="to get user's telegram")
@click.option("--name", help="this command is based on name")
def get_telegram(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\ntelegram is {p.telegram} and the telegram link is https://t.me/{p.telegram}")
        else:
            print("[*] not found in contact! [*]")

@click.command(help="to get user's instagram")
@click.option("--name", help="this command is based on name")
def get_instagram(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\ninstagram is {p.instagram} and the instagram link is https://instagram.com/{p.instagram}")
        else:
            print("[*] not found in contact! [*]")

@click.command(help="to get user's twitter")
@click.option("--name", help="this command is based on name")
def get_twitter(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\ntwitter is {p.twitter} and the twitter link is https://twitter.com/{p.twitter}")
        else:
            print("[*] not found in contact! [*]")

@click.command(help="to get user's github")
@click.option("--name", help="this command is based on name")
def get_github(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\ngithub is {p.github} and the github link is https://github.com/{p.github}")
        else:
            print("[*] not found in contact! [*]")

@click.command(help="to get user's linkedin")
@click.option("--name", help="this command is based on name")
def get_linkedin(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\nlinkedin is {p.linkedin} and the linkedin link is https://linkedin.com/{p.linkedin}")
        else:
            print("[*] not found in contact! [*]")
            

group.add_command(get_user)
group.add_command(add_user)
group.add_command(get_number)
group.add_command(get_email)
group.add_command(get_telegram)
group.add_command(get_instagram)
group.add_command(get_twitter)
group.add_command(get_github)
group.add_command(get_linkedin)
if __name__ == "__main__":
    group()
