import unittest

from whiteboard import is_defended


class Test_Is_Defended(unittest.TestCase):




    def test_attackers_win(self):
        result = is_defended([ 2, 4, 6, 8 ],[ 1, 3, 5, 7 ])
        self.assertFalse(result)

    def test_defenders_win(self):
        self.assertTrue(is_defended([ 1, 3, 5, 7 ],[ 2, 4, 6, 8 ]))
    
    def test_attack_power(self):
        result = is_defended([ 1, 3, 5, 7 ],[ 2, 4, 1, 1 ])
        self.assertFalse(result)
        defenders_win = is_defended([ 2, 4, 1, 1 ],[ 1, 3, 5, 7 ])
        self.assertTrue(defenders_win)
    
    def test_uneven_team_lengths(self):
        attackers_win = is_defended([1,3,5,7,1],[2,4])
        defenders_win = is_defended([2,3],[1,3,5,7,1])
        self.assertTrue(defenders_win)
        self.assertFalse(attackers_win)

if __name__ == '__main__':
    unittest.main()