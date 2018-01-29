import io
def test_charcount():
	file=io.open("task2/input.txt","r",encoding="utf-8")
	assert len(file.read().strip('\n'))==6
