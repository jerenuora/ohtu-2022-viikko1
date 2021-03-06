import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_tilavuus_varasto = Varasto(-1)
        self.alkusaldollinen_varasto = Varasto(10,11)
        self.alkusaldollinen_varasto_neg = Varasto(10,-11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_ei_negatiivista_varaston(self):
        self.assertAlmostEqual(self.neg_tilavuus_varasto.tilavuus, 0)
        # saldo näköjään menee silti miinukselle?
        self.assertAlmostEqual(self.neg_tilavuus_varasto.saldo, -1)

    def test_konstruktori_luo_täyden_varaston_ei_liikaa(self):
        self.assertAlmostEqual(self.alkusaldollinen_varasto.saldo, 10)

    def test_konstruktori_luo_ei_negatiivis_saldoisen_varaston(self):
        self.assertAlmostEqual(self.alkusaldollinen_varasto_neg.saldo, 0)


    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liikaa_lisays_lisaa_saldoa_ei_liikaa(self):
        self.varasto.lisaa_varastoon(80)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(-80)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_liikaa_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_negatiivinen_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_str_toimii(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")