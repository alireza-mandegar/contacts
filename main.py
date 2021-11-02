import click


@click.group()
def group():
    pass


class Person:
    def __init__(self, name, number, email, telegram, instagram, twitter, github, linkedin):
        self.name = name
        self.number = number
        self.email = email
        self.telegram = telegram
        self.instagram = instagram
        self.twitter = twitter
        self.github = github
        self.linkedin = linkedin

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_email(self):
        return self.email

    def get_telegram(self):
        return self.telegram

    def get_telegram_link(self):
        return f"t.me/{self.telegram}"

    def get_instagram(self):
        return self.instagram

    def get_instagram_link(self):
        return f"instagram.com/{self.instagram}"

    def get_twitter(self):
        return self.twitter

    def get_twitter_link(self):
        return f"twitter.com/{self.twitter}"

    def get_github(self):
        return self.github

    def get_github_link(self):
        return f"github.com/{self.github}"

    def get_linkedin(self):
        return self.linkedin

    def get_linkedin_link(self):
        return f"linkedin.com/{self.linkedin}"


def main():
    p = Person("alireza", "09221235677", "alireza.mani95@gmail.com", "alireza_mandegar",
               "alirezaamandegar", "alirzamandegar", "alireza-mandegar", "alirezamandegar")


if __name__ == "__main__":
    pass
