def test_charcount():
	file=open("input.txt","r",encoding="utf-8")
	assert len(file.read().strip('\n'))==6
