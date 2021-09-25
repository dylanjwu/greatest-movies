from MovieList import MovieList

url_file = open("urls.txt", "r") 
URLS = [line for line in url_file.read().split('\n')]

QUERIES = [
".ct-slideshow__slide__text-container__caption div",
".lister-list .titleColumn",
"._h3_cuogz_1",
".q_title",
"h3",
".sc-AxhUy",
]

PATTERNS = [
 '#([0-9]{1,3})\.\s(.+)\s\(([0-9]{4})\)',
 '\\n\s*([0-9]*)\.\\n\s*(.*)\\n\(([0-9]{4})\).*',
 '([0-9]*)\.\\.*\s*(.*)\s\(([0-9]{4})\)',
 '([0-9]*).\s(.*)\s\(([0-9]{4})\)',
 '([0-9]*)\.\s*(.*)\s\(([0-9]{4})\).*',
 ''
]

LISTS = []
for i in range(len(URLS)):
    LISTS.append({'url': URLS[i], 'query': QUERIES[i], 'pattern': PATTERNS[i]})

def get_list1():
    l = MovieList(LISTS[0])
    return l.parse_movies()

def get_list():
    l = MovieList(LISTS[4])
    return l.parse_movies()


def get_master_collection():
    master_collection = {}
    for j in range(0,len(LISTS)-1): #excluding last list, which has no pattern yet
        l = MovieList(LISTS[j])
        parsed_movies = l.parse_movies()
        for movie in parsed_movies:
            if movie['title'] not in master_collection:
                master_collection[movie['title']] = {'rankings': {j: movie['rank']}, 'year': movie['year']}
            else:
                master_collection.get(movie['title'])['rankings'][j] = movie['rank']

    for key,value in master_collection.items():
        if len(value['rankings']) >= 5:
            avg_rank = sum([int(a) for a in value['rankings'].values()])/len(value['rankings'])
        else: 
            avg_rank = 101
        master_collection[key]['avg_rank'] = avg_rank
    
    return master_collection

master_collection = get_master_collection()

sorted_collection = sorted(master_collection.items(), key=lambda item: item[1]['avg_rank'])
total=0
for key,val in master_collection.items():
    if len(val['rankings']) >= 3:
        total+=1
        print(key, val)
print(total)
sorted_list = [key for key,val in sorted_collection]
# print(sorted_list[:100])




