from pathlib import Path

years = {
    "2025":
        ["", "", "", "", "", ""]
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
}

header = ["Year", "D1-1", "D1-2", "D1-3", "D2-1", "D2-2", "D2-3", "", ""]

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
