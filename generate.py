from pathlib import Path

years = {
    "2025":
        [("Souvenirs*", "https://codeforces.com/blog/entry/145172?#comment-1298794"), ("Triples*", "https://codeforces.com/blog/entry/145172?#comment-1298794"), ("World Map*", "https://codeforces.com/blog/entry/145172?#comment-1298794"), ("Festivals*", "https://codeforces.com/blog/entry/145172?#comment-1299575"), ("Migrations*", "https://codeforces.com/blog/entry/145228"), ("Obstacles*", "https://codeforces.com/blog/entry/145172?#comment-1299575")]
    ,
    "2024":
        ["Nile", "Message", "Tree", "Hieroglyphs", "Mosaic", "Sphinx"]
    ,
    "2023":
        [("Closing Time*", "https://danielz.fyi/thoughts/closing-time"), ("Longest Trip*", "https://blog.brucemerry.org.za/2023/11/ioi-2023-day-1.html"), ("Soccer Stadium*", "https://blog.brucemerry.org.za/2023/11/ioi-2023-day-1.html"), ("Beech Tree*", "https://blog.brucemerry.org.za/2023/11/ioi-2023-beech-tree.html"), ("Overtaking*", "https://blog.brucemerry.org.za/2023/12/ioi-2023-overtaking.html"), ("Robot Contest*", "https://codeforces.com/blog/entry/120252")]
    ,
    "2022":
        [("Catfish Farm", "editorial.pdf"), ("Prisoner Challenge", "editorial.pdf"), ("Radio Towers", "editorial.pdf"), ("Digital Circuit", "editorial.pdf"), ("Rarest Insects", "editorial.pdf"), ("Thousands Islands", "editorial.pdf")]
    ,
    "2021":
        [("Distributing Candies", "candies.pdf"), ("Keys", "keys.pdf"), ("Fountain Parks", "parks.pdf"), ("Mutating DNA", "dna.pdf"), ("Dungeons Game", "dungeons.pdf"), ("Bit Shift Registers", "registers.pdf")]
    ,
    "2020":
        [("Comparing Plants", "plants.pdf"), ("Connecting Supertrees", "supertrees.pdf"), ("Carnival Tickets", "tickets.pdf"), ("Packing Biscuits", "biscuits.pdf"), ("Counting Mushrooms", "mushrooms.pdf"), ("Stations", "stations.pdf")]
    ,
    "2019":
        [("Arranging Shoes", "shoes.pdf"), ("Split the Attractions", "split.pdf"), ("Rectangles", "rect.pdf"), ("Broken Line", "line.pdf"), ("Vision Program", "vision.pdf"), ("Sky Walking", "walk.pdf")]
    ,
    "2018":
        ["Combo", "Seats", "Werewolf", ("Mechanical Doll", "doll.pdf"), ("Highway Tolls", "highway.pdf"), "Meetings"]
    ,
    "2017":
        ["Nowruz", "Wiring", ("Toy Train", "train.pdf"), ("The Big Prize", "prize.pdf"), "Simurgh", ("Ancient Books", "books.pdf")]
    ,
    "2016":
        [("Detecting Molecules", "editorial.pdf"), ("Roller Coaster Railroad", "editorial.pdf"), ("Shortcut", "editorial.pdf"), ("Paint By Numbers", "editorial.pdf"), ("Unscrambling a Messy Bug", "editorial.pdf"), ("Aliens", "editorial.pdf")]
    ,
    "2015":
        [("Boxes with souvenirs", "boxes.pdf"), ("Scales", "scales.pdf"), ("Teams", "teams.pdf"), ("Horses", "horses.pdf"), ("Sorting", "sorting.pdf"), ("Towms", "towns.pdf")]
    ,
    "2014":
        ["Rail", "Wall", "Game", "Gondola", "Friend", "Holiday"]
    ,
    "2013":
        [("Art Class*", "https://blog.brucemerry.org.za/2013/07/ioi-2013-day-1-analysis.html"), ("Dreaming", "https://blog.brucemerry.org.za/2013/07/ioi-2013-day-1-analysis.html"), ("Wombats", "https://blog.brucemerry.org.za/2013/07/ioi-2013-day-1-analysis.html"), ("Cave*", "https://blog.brucemerry.org.za/2013/07/ioi-2013-day-2-analysis.html"), ("Robots", "https://blog.brucemerry.org.za/2013/07/ioi-2013-day-2-analysis.html"), ("Game*", "https://usaco.guide/problems/ioi-2013game/solution")]
    ,
    "2012":
        [("Parachute rings", "editorial.pdf"), ("Pebbling odometer", "editorial.pdf"), ("Crayfish scrivener", "editorial.pdf"), ("Ideal city", "editorial.pdf"), ("Last Supper", "editorial.pdf"), ("Jousting tournament", "editorial.pdf")]
    ,
    "2011":
        [("Tropical Garden", "garden.pdf"), "Race", "Rice Hub", ("Crocodile's Underground City", "crocodile.pdf"), ("Dancing Elephants", "elephants.pdf"), "Parrots"]
    ,
}

header = ["Year", "D1-1", "D1-2", "D1-3", "D2-1", "D2-2", "D2-3"]

print("""Legend:
- X: missing
- *: unofficial
- (t) translated
- (u) untranslated, not in English

Please contact me if you have any of the missing editorials.
Also feel free to contact me if you believe you have a better version of any of the unofficial ones.
""")

print("| " + " | ".join(header) + " |")
print("|" + "|".join(["------"] * len(header)) + "|")

extensions = ["pdf", "md", "txt"]
def format_url(year, task):
    task_name = None
    task_url = None
    if isinstance(task, str):
        task_name = task
    else:
        task_name = task[0]

    suffix = ""
    for mark in ["(u)", "(t)", "*"]:
        if mark in task_name:
            suffix += mark
            task_name = task_name.replace(mark, "")
    
    if isinstance(task, str):
        task_shortname = ''.join(task_name.split()).lower()
        for ext in extensions:
            if (Path("editions") / year / f"{task_shortname}.{ext}").exists():
                extension = ext
                break
        else:
            assert 0, f"Nothing for {year}/{task_name}"
        task_url = f"editions/{year}/{task_shortname}.{extension}"
    else:
        if "https" in task[1]:
            task_url = task[1]
        else:
            task_url = f"editions/{year}/{task[1]}"

    return f"[{task_name}]({task_url}){suffix}"

tot = 0
has = 0
for year, p_list in years.items():
    if len(p_list) == 0:
        continue
    tasks = []
    if len(p_list) in (6, 8):
        tasks = p_list
    elif len(p_list) == 1:
        tasks = [p_list[0]] * 6
    else:
        assert 0
    row = [year]

    for task in tasks:
        tot += 1
        if task:
            if "(u)" not in task:
                has += 1
            row.append(format_url(year, task))
        else:
            row.append("X")
    
    print("| " + " | ".join(row) + " |")

print(f"\n\nProgress: {has/tot*100:.2f}% ({has}/{tot})")
