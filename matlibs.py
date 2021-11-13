from random import randint
import copy

story = (
        "one fine day me and my friend {} decided to go to {}. " +
        "there we found a {} and played with that {} {}, " +
        "and my friend {} is like {}. " +
        "we enjoyed a lot in {}. " +
        "i was very {} and uncontrollable to the {}. "
)

word_dic = {
    "name": ['anvesh', 'virat', 'rakul', 'sniggy', 'samantha', 'nani', 'kajal'],
    "place": ['hyderabad', 'mumbai', 'karnataka', 'kerala', 'delhi', 'park'],
    "animal": ['dog', 'pig', 'ant', 'grassopper', 'kitten', 'rabbit'],
    "thing": ['stick', 'bat', 'ball', 'tub', 'stool'],
    "emotion": ['happy', 'sad', 'disgusting', 'anger', 'emotional', 'juicy'],
    "expression": ['woww', 'hurrey', 'ufffuuuu', 'sexyyyy boyyy', 'nice onee'],
    "experience": ["good", 'best', 'better', 'ok']

}


def get_word(type, local_dict):
    words = local_dict[type]
    count = len(words) - 1
    index = randint(0, count)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dic)
    return story.format(
        get_word("name", local_dict),
        get_word("expression", local_dict),
        get_word("place", local_dict),
        get_word("name", local_dict),
        get_word("animal", local_dict),
        get_word("thing", local_dict),
        get_word("emotion", local_dict),
        get_word("name", local_dict),
        get_word("experience", local_dict),
        get_word("animal", local_dict),
        get_word("thing", local_dict)


    )


print("story 1 : ")
print(create_story())
print()
print("story 2 :")
print(create_story())
print()
print("story 3 :")
print(create_story())