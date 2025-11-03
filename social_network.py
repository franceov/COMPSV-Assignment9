class Person:
    def __init__(self, name: str):
        self.name = name
        self.friends = []  # list[Person]

    def add_friend(self, friend: "Person") -> None:
        # prevent duplicates and self-friendship
        if friend is self:
            return
        if all(f is not friend for f in self.friends):
            self.friends.append(friend)

    def friend_names(self):
        return [f.name for f in self.friends]


class SocialNetwork:
    def __init__(self):
        # adjacency list: name -> Person instance
        self.people = {}  # dict[str, Person]

    def add_person(self, name: str) -> None:
        if name in self.people:
            print(f"Person '{name}' already exists. Skipping.")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name: str, person2_name: str) -> None:
        if person1_name == person2_name:
            print("Friendship not created. A person cannot friend themselves.")
            return

        p1 = self.people.get(person1_name)
        p2 = self.people.get(person2_name)

        if p1 is None or p2 is None:
            missing = [n for n, p in [(person1_name, p1), (person2_name, p2)] if p is None]
            print(f"Friendship not created. {', '.join(missing)} {'does' if len(missing)==1 else 'do'}n't exist!")
            return

        # bidirectional edge
        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self) -> None:
        # deterministic output: sort by person name, and each friend list sorted by name
        for name in sorted(self.people.keys()):
            person = self.people[name]
            friends_sorted = sorted(person.friend_names())
            if friends_sorted:
                print(f"{name} is friends with: {', '.join(friends_sorted)}")
            else:
                print(f"{name} is friends with: ")

if __name__ == "__main__":
    network = SocialNetwork()

    # Add people (>=6)
    for n in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(n)

    # Edge cases
    network.add_person("Alex")  # duplicate
    network.add_friendship("Jordan", "Johnny")  # missing person
    network.add_friendship("Alex", "Alex")  # self-friend

    # Create friendships (>=8)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Print the network
    network.print_network()

"""
DESIGN MEMO (also provided in DESIGN_MEMO.txt):

See DESIGN_MEMO.txt for a 200–300 word reflection on structure choices, trade-offs, and performance.
"""


# Test your code here
