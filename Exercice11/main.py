# Écrivez votre code ici !
from dataclasses import dataclass


@dataclass
class BankAccount:
    """
    Classe représentant un compte bancaire.

    Attributs:
        account_holder (string): le nom du titulaire du compte.
        balance (float): le solde du compte.

    Méthodes:
        display_details(): Affiche les attribut de Person
    """
    account_holder: str
    balance: float

    def deposit(self, amount):
        """pour déposer de l'argent sur le compte """
        self.balance += amount
        print(f"vous avez ajoutez {amount}£ à votre compte, le solde de votre compte est maintenant de {self.balance}£")

    def withdraw(self, amount):
        """pour retirer de l'argent du compte"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"Vous avez retirez la somme de {amount}£, votre nouveau solde est de {self.balance}£")
        else:
            print(f"Fonds insuffisants. Solde actuel : {self.balance}£")

    def display_balance(self):
        """pour afficher le solde et le nom du propriétaire du compte."""
        print(f"""Le solde du compte est de {self.balance}£ \n"""
              f"""Le propriétaire du compte est M ou Mme {self.account_holder}""")


Account1 = BankAccount(account_holder="BOB" , balance=15000)
Account2 = BankAccount(account_holder="JHON" , balance=500)

Account1.display_balance()
Account1.deposit(2000)
Account1.withdraw(17000)

Account2.display_balance()
Account2.withdraw(1000)
