Shakespear="""She speaks:
O, speak again, bright angel! for thou art
As glorious to this night, being o'er my head
As is a winged messenger of heaven
Unto the white-upturned wondering eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy-pacing clouds
And sails upon the bosom of the air."""

Ralph="""The new life to which he had been called opened pleasantly and increased in happiness and opportunity,
except for the sadness of bereavements, for, in the first few years,
his brilliant brothers Edward and Charles died, and soon afterward Waldo, his firstborn son,
and later his mother. Emerson had left traditional religion,
the city, the Old World, behind, and now went to Nature as his teacher, his inspiration.
His first book, "Nature," which he was meditating while in Europe, was finished here, and published in 1836.
His practice during all his life in Concord was to go alone to the woods almost daily,
sometimes to wait there for hours, and, when thus attuned, to receive the message to which he was to give voice.
Though it might be colored by him in transmission, he held that the light was universal."""

Shakespear_list=Shakespear.split()
Ralph_list=Ralph.split()

for i in Ralph_list:
    if i in Shakespear_list:
        print("общее слово = ",i)
    else:
        print("уникальное слово ",i)