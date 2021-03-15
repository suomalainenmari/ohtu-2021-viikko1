import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_negatiivista_tilavuus_konstruktorissa_asetetaan_nollaksi(self):
      testi = Varasto (-3)
      self.assertAlmostEqual(testi.tilavuus, 0)
    
    def test_negatiivista_saldo_konstruktorissa_asetetaan_nollaksi(self):
      testi = Varasto (10,-5)
      self.assertAlmostEqual(testi.saldo, 0)

    def test_lisaa_negatiivinen_luku_varastoon(self):
      self.varasto.lisaa_varastoon(-5)
      self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_enemman_kun_mahtuu(self):
      self.varasto.lisaa_varastoon(12)
      self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen_luku(self):
      self.varasto.lisaa_varastoon(8)
      self.varasto.ota_varastosta(-2)
      self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ota_enemman_kun_saldo(self):
      self.varasto.lisaa_varastoon(5)
      self.varasto.ota_varastosta(6)
      self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tulostus_tulee_oikein(self):
      self.assertAlmostEqual(str(self.varasto),"saldo = 0, vielä tilaa 10")

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

