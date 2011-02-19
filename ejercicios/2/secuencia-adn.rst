Secuencia de ADN
----------------

Realice una función con la que se pueda buscar
una subsecuencia determinada en una gran
secuencia de ADN, entregada por el usuario.

Considere la siguiente secuencia::

	gtgggggggtttatgcctttagaacagcagactactgataactccaatcctgggttgaaa
	atgccaagggcgccagagagccaaacgatgagcgttggaccacaaacgataaaaactcac
	tttctccgtggggtgaaagcgattctttctggcccgtatccgccagcacttaaagttgca
	ttcggcgcggccctaccgctgctaattggggtaattgtcctaggattgtacgtaacgctt
	ggcgggcacagccgcaagaaagcccacgcagccgcgatagatgctttggtcgagaagcac
	gaagcatgctacaaggtccaagcaaagattgcacacggcaggcttgccttacagtccgct
	gtggtgtctgttgcggatgccagcatgcaacaactccagttcgtgcagcaaggaattctc
	atgtgtgtcggagagctcgacgatatgcagaagttccggacccgactggataatgaaatc
	agtgccatcaaccagcgaattcccagcattgtcgaggaggtaagaaaacacaccgacgat
	gcgcttgagtggaatcttgctagaaccaagaacattttagagggcactgaagagcgcctg
	aaggatatgggcaatgagttggtgcgctacctagacgatgctcgcgccctcattgaaaat
	gcacgtatagctgcaggatcaatgcaacacctcgttggtgatgaggtgagaaagcagctt
	gctgaggttctagtaaaagttgcagaagtaagtaatggctttattgcgcttaagaagagt
	gtatctggctatttggaaaaaagcagtggacttgttgctagggaagttagggcaatcctg
	gatgaccgcatgcgaagcctgcggaccatgtacaaaatgtgggatgcagaacaaaactcc
	gtagtcagcgtgtgtaccacgctccaaaaggcaagcatggaggctgccgcggtagcaagt


Recuerde la sentencia *in*.

::

	esta_en_adn("ttt",secuencia)
	True

::

	esta_en_adn("aaaaaa",secuencia)
	True

::

	esta_en_adn("hola",secuencia)
	False

