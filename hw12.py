import random
class Member:
    '''
    Purpose: this is repsensents the people playing the game and stores their infromation
    Instance variables: name stores their name as a string and socialStatus that is thier odds of getting voted out
    Methods: init constructs the class and sets baselines, updateStatus is how status is determined by capping it and
    randomly rolling each time, repr is just an override that returns a string of a name and status
    '''
    def __init__(self,name):
        self.name = str(name)
        self.socialStatus = 5

    def updateStatus(self):
        coin_flip = random.randint(0,1)
        if self.socialStatus == 10:
            self.socialStatus = 10
        elif self.socialStatus == 1:
            self.socialStatus = 1
        else:
            if coin_flip == 1:
                self.socialStatus -= 1
            else:
                self.socialStatus += 1

    def __repr__(self):
        return ("Name: {}, Social Status: {}".format(self.name, self.socialStatus))

class Tribe:
    '''
    Purpose: this repersents the tribes with members in them
    Instance variables: tribeName repsersents the tribes name and members which repsersents people and their status
    Methods: init that just constructs the class and updateStatusForAll that changes the social status of everyone in the tribe
    '''

    def __init__(self,tribeName,playerNames):
        self.tribeName = str(tribeName)
        self.members = []
        for player in playerNames:
            self.members.append(Member(player))

    def updateStatusForAll(self):
        for member in self.members:
            member.updateStatus()

# PART B (20 points)
#########################################################################

class Game:
    #Be sure to fill out the documentation for each class, including this one
    '''
    Purpose: this repsents the different elements that take place in the game
    Instance variables: the instance varibles are merge,redTribe, and blueTribe that repesent the tribes while playing the game
    Methods: the init fuction which constructs the basics, challengeWinner which chooses a random winner from a given set,
    getOdds which generates the odds of a perosn being voted out, vote which randomly chooses someone and removes them from the tribes
    lastly playSurvivor which combines everything and runs them as a simulation
    '''
    def __init__(self, redTribe, blueTribe):
        self.redTribe = redTribe
        self.blueTribe = blueTribe
        self.merge = Tribe('Merged Tribe', [])


    def challengeWinner(self):
        if self.merge.members != []:
            winner = self.merge.members[random.randint(0, len(self.merge.members) - 1)]
            print('{} wins the challenge!'.format(winner.name))
            return str(winner.name)
        else:
            winner = random.randint(0,1)
            if winner == 0:
                print('Red Tribe wins the challenge!')
                return 'Red Tribe'
            else:
                print('Blue Tribe wins the challenge!')
                return 'Blue Tribe'

    def getOdds(self, tribe):
        odds = []
        for member in tribe.members:
            name = [member.name]
            name = [member.name] * member.socialStatus
            odds += name
        return odds

    def vote(self, tribe, immune):
        vote_out = random.choice(self.getOdds(tribe))
        while vote_out == immune:
            vote_out = random.choice(self.getOdds(tribe))
        if len(tribe.members) == 2:
            for member in tribe.members:
                if member.name != vote_out:
                    print('The sole survivor is {}'.format(member.name))
                    return member.name
        for member in tribe.members:
            if member.name == vote_out:
                tribe.members.remove(member)
        print('{} voted out of the {}'.format(vote_out,tribe.tribeName))
        return vote_out

    def playSurvivor(self):
        round_count = 0
        round_count_merge = 0
        while round_count < 4:
            winner = self.challengeWinner()
            if winner == 'Red Tribe':
                self.vote(self.blueTribe,"")
                self.blueTribe.updateStatusForAll()
                self.redTribe.updateStatusForAll()
            else:
                self.vote(self.redTribe,"")
                self.blueTribe.updateStatusForAll()
                self.redTribe.updateStatusForAll()
            round_count += 1
        for member in self.redTribe.members:
            self.merge.members.append(member)
        for member in self.blueTribe.members:
            self.merge.members.append(member)
        while round_count_merge < 6:
            winner = self.challengeWinner()
            self.vote(self.merge, winner)
            self.merge.updateStatusForAll()
            round_count_merge += 1
        self.vote(self.merge, "")
#########################################################################

def main():
    names = ["Isaac", "Arunima", "Nakul", "Micah", "David", "Alice",
            "Tarik", "Ian", "Charley", "Demond", "Abdourahman", "Vin"]
    redTribeNames = []

    while len(redTribeNames) < 6:
        randName = random.choice(names)
        redTribeNames.append(randName)
        names.remove(randName)

    blueTribeNames = names

    #UNCOMMENT THE FOLLOWING TO CREATE TRIBES AND TEST THE SIMULATION
    redTribe = Tribe("Red Tribe", redTribeNames)
    blueTribe = Tribe("Blue Tribe", blueTribeNames)

    simulation = Game(redTribe, blueTribe)
    simulation.playSurvivor()

if __name__ == '__main__':
    main()
