import random
import time

# --- TICKET #2: DESIGN THE BLUEPRINT ---
class BattleBot:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.strength = random.randint(10, 20)  # RNG Strength
        self.defense = random.randint(0, 5)     # RNG Defense
        
        print(f"🤖 FACTORY: Built {self.name} | STR: {self.strength} | DEF: {self.defense}")

    # --- TICKET #3: COMBAT LOGIC ---
    def attack(self, enemy):
        print(f"\n⚔️ {self.name} attacks {enemy.name}!")
        time.sleep(1) # Suspense

        # Calculate Damage
        damage = self.strength - enemy.defense
        
        # Critical Hit Logic (20% chance)
        if random.randint(1, 100) > 80:
            damage = damage * 2
            print("   🔥 CRITICAL HIT! Double Damage! 🔥")

        # Prevent negative damage (healing the enemy)
        damage = max(0, damage)

        # Apply the hit
        enemy.take_damage(damage)

    def take_damage(self, amount):
        self.current_health -= amount
        print(f"   💥 {self.name} took {amount} damage!")
        print(f"   ❤️ Health: {self.current_health}/{self.max_health}")

    def is_alive(self):
        return self.current_health > 0

# --- TICKET #4: THE BATTLE LOOP ---
# (Joel, you run this part after importing their bots)
if __name__ == "__main__":
    print("📢 WELCOME TO THE INNOVATION CENTRE FIGHT CLUB 📢")
    
    # Spawn the Fighters
    bot1 = BattleBot("Terminator")
    bot2 = BattleBot("Wall-E")

    round_num = 1

    # Fight until one dies
    while bot1.is_alive() and bot2.is_alive():
        print(f"\n--- ROUND {round_num} ---")
        
        bot1.attack(bot2)
        
        # Check if bot2 survived before counter-attacking
        if bot2.is_alive():
            bot2.attack(bot1)

        round_num += 1
        time.sleep(1.5)

    print("\n🏆 GAME OVER 🏆")
    if bot1.is_alive():
        print(f"🎉 {bot1.name} WINS!")
    else:
        print(f"🎉 {bot2.name} WINS!")
