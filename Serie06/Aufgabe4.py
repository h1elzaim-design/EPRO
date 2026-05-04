words = ["Python", "Java", "C++", "JavaScript", "Ruby", "Linux", "Windows", "MacOS", "Ubuntu", "Fedora", "Arch", "Debian", "Mint", "Manjaro", "Raspbian", "CentOS"]

def favourite_sort(words, fav_chars='aeiouAEIOU'):
    return sorted(words,
                    key=lambda w: sum(1 for c in w if c in fav_chars),
                    reverse=True )    

print(favourite_sort(words))

# key=lambda definiert wie es sortiert wird, in dem Fall nach den meisten Vokalen
