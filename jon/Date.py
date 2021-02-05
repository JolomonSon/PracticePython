class Nfs():
    def join(self):
        print('You have joined the game')

class Halo():
    def home(self):
        print("You are in your home")
    def shoot(self):
        print("You have being shot once")

class clas(Nfs, Halo):
    pass

game = clas()

game.home()
game.join()
game.shoot()
