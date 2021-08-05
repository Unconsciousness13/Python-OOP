from project.hero import Hero
import unittest


class YestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Pako", 9, 100, 50)

    def test_initial_class_attributes(self):
        self.assertEqual("Pako", self.hero.username)
        self.assertEqual(9, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)


    def test_pako_ako_se_bie_sreshtu_sebe_si(self):
        pako = Hero('Pako', 9, 100, 50)
        with self.assertRaises(Exception):
            self.hero.battle(pako)

    def test_if_your_hero_is_with_negative_hp(self):
        self.hero.health = -5
        enemy = Hero("Enemy", 5, 50, 20)
        with self.assertRaises(ValueError):
            self.hero.battle(enemy)

    def test_if_your_hero_is_with_zero_hp(self):
        enemy = Hero("Enemy", 5, 50, 20)
        self.hero.health = 0
        with self.assertRaises(ValueError):
            self.hero.battle(enemy)

    def test_enemy_hero_when_negative_hp(self):
        enemy = Hero("Enemy", 5, 1, 20)
        enemy.health = -10
        with self.assertRaises(ValueError):
            self.hero.battle(enemy)

    def test_if_enemy_is_with_zero_hp(self):
        enemy = Hero("Enemy", 5, 1, 20)
        enemy.health = 0
        with self.assertRaises(ValueError):
            self.hero.battle(enemy)



    def test_hero_battle_damage(self):
        smrado = Hero('smrado', 1, 12, 11)
        smrado_health = -438
        self.hero.battle(smrado)
        self.assertEqual(smrado_health, smrado.health)

    def test_if_battle_is_won(self):
        vrag = Hero('Pustinqk', 2, 10, 2)
        o_message = self.hero.battle(vrag)
        self.assertTrue(vrag.health <= 0)
        self.assertEqual('You win', o_message)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(101, self.hero.health)

    def test_if_battle_is_lost(self):
        qze = Hero("qze", 1, 2, 2)
        vrago = Hero('Pomiar', 24, 233, 99)
        o_message = qze.battle(vrago)
        self.assertTrue(qze.health <= 0)
        self.assertEqual('You lose', o_message)
        self.assertEqual(25, vrago.level)
        self.assertEqual(104, vrago.damage)
        self.assertEqual(236, vrago.health)

    def test_if_battle_is_draw(self):
        vrag = Hero('tigar', 9, 100, 50)
        o_mess = self.hero.battle(vrag)
        self.assertTrue(self.hero.health <= 0)
        self.assertTrue(vrag.health <= 0)
        self.assertEqual('Draw', o_mess)

    def test_for_final_result_as_string(self):
        result = f"Hero Pako: 9 lvl\n" \
                 f"Health: 100\n" \
                 f"Damage: 50\n"
        self.assertEqual(result, str(self.hero))


if __name__ == "__main__":
    unittest.main()

