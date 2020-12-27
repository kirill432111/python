count = 0
c = {}
text = """She speaks:
O, speak again, bright angel! for thou art
As glorious to this night, being o'er my head
As is a winged messenger of heaven
Unto the white-upturned wondering eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy-pacing clouds
And sails upon the bosom of the air."""
text = text.split()
for i in text:
    for j in text:
        if i == j:
            count = count + 1
            c[i] = (count)

    count = 0

print("Подсчет повторений каждого слова в абзаце")
print(c)
print()