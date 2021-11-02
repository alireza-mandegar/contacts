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


# p = Person("alireza", "09123456789", "alireza.mani95@gmail.com", "alireza_mandegar",
#            "alirezaamandegar", "alirzamandegar", "alireza-mandegar", "alirezamandegar")

con = sqlite3.connect("./contact.db")
cur = con.cursor()
# cur.execute('''CREATE TABLE contact
#                 (name, number, email, telegram, instagram, twitter, github, linkedin)''')


@click.command(help="to update number in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_number")
def change_number(name, new_number):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set number = '{new_number}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new number is {new_number} [*]]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update email in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_email")
def change_email(name, new_email):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set email = '{new_email}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new email is {new_email} [*]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update telegram in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_telegram")
def change_telegram(name, new_telegram):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set telegram = '{new_telegram}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new telegram is {new_telegram} [*]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update instagram in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_instagram")
def change_instagram(name, new_instagram):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set instagram = '{new_instagram}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new instagram is {new_instagram} [*]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update twitter in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_twitter")
def change_twitter(name, new_twitter):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set twitter = '{new_twitter}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new twitter is {new_twitter} [*]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update github in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_github")
def change_github(name, new_github):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set github = '{new_github}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new github is {new_github} [*]")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to update linkedin in your contact")
@click.option("--name", help="this command is based on name")
@click.argument("new_linkedin")
def change_linkedin(name, new_linkedin):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            cur.execute(
                f"UPDATE contact set linkedin = '{new_linkedin}' where name = '{name}'")
            con.commit()
            print(
                f"[*] the contact has been updated! [*]\n[*] new linkedin is {new_linkedin} [*]")
            return
    print("[*] not found in contact! [*]")


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
    for row in cur.execute(f'SELECT * FROM contact ORDER BY name'):
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
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's number")
@click.option("--name", help="this command is based on name")
def get_number(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\nnumber is {p.number}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's email")
@click.option("--name", help="this command is based on name")
def get_email(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(f"name is {p.name}\nemail is {p.email}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's telegram")
@click.option("--name", help="this command is based on name")
def get_telegram(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(
                f"name is {p.name}\ntelegram is {p.telegram} and the telegram link is https://t.me/{p.telegram}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's instagram")
@click.option("--name", help="this command is based on name")
def get_instagram(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(
                f"name is {p.name}\ninstagram is {p.instagram} and the instagram link is https://instagram.com/{p.instagram}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's twitter")
@click.option("--name", help="this command is based on name")
def get_twitter(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(
                f"name is {p.name}\ntwitter is {p.twitter} and the twitter link is https://twitter.com/{p.twitter}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's github")
@click.option("--name", help="this command is based on name")
def get_github(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(
                f"name is {p.name}\ngithub is {p.github} and the github link is https://github.com/{p.github}")
            return
    print("[*] not found in contact! [*]")


@click.command(help="to get user's linkedin")
@click.option("--name", help="this command is based on name")
def get_linkedin(name):
    for row in cur.execute(F'SELECT * FROM contact ORDER BY name'):
        if row[0] == name:
            p = Person(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])
            print(
                f"name is {p.name}\nlinkedin is {p.linkedin} and the linkedin link is https://linkedin.com/{p.linkedin}")
            return
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
group.add_command(change_number)
group.add_command(change_email)
group.add_command(change_telegram)
group.add_command(change_instagram)
group.add_command(change_twitter)
group.add_command(change_github)
group.add_command(change_linkedin)
if __name__ == "__main__":
    group()
