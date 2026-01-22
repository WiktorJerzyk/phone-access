import os
import html

# --- KONFIGURACJA (Zastępuje oddzielne pliki properties i links dla wygody) ---
folder_properties = {
    "Fizyka": {"priority": 2, "show": True, "id": "fizyka"},
    "Informatyka": {"priority": 3, "show": True, "id": "informatyka"},
    "Angielski": {"priority": 3, "show": True, "id": "angielski"},
    "Polski": {"priority": 3, "show": True, "id": "polski"},
    "Matma": {"priority": 1, "show": True, "id": "matma"},
    "Const": {"priority": 6, "show": True, "id": "const"},
}

folder_links = {
    "Matma": [
        {"name": "Khan Academy - Matematyka", "url": "https://pl.khanacademy.org/math"},
        {"name": "Matemaks", "url": "https://matemaks.pl/"},
        {"name": "Zadania.info", "url": "https://zadania.info/d1"},
    ],
    "Fizyka": [
        {"name": "Fizyka Jamnika", "url": "https://fizyka.org/?teoria,0"},
        {"name": "Fizyka Baza maturalna", "url": "https://matura100procent.pl/zadania-maturalne/baza-zadan-maturalnych/baza-zadan-z-fizyki/"},
        {"name": "eFizyka", "url": "https://www.e-fizyka.pl/"},
        {"name": "Filoma", "url": "https://www.filoma.org/fizyka"},
        {"name": "Zadania dlamaturzysty info", "url": "https://zadania.dlamaturzysty.info/s/4981/80948-fizyka.htm"},
        {"name": "Efizyka net", "url": "https://efizyka.net.pl/dzialy-fizyki"}
    ],
    "Angielski": [
        {"name": "Grammarly", "url": "https://www.grammarly.com"},
        {"name": "Odpowiedzi do repetytorium", "url":"https://www.gotowiec.pl/jezyk-angielski/repetytorium-podrecznik-do-szkol-ponadpodstawowych-matura-2023-poziom-podstawowy-i-rozszerzony2"}
    ],
    "Const": [
        {"name": "Komunikaty CKE Rok szkolny 2025/2026", "url": "https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/harmonogram-komunikaty-i-informacje/rok-szkolny-2025-2026/"},
        {"name": "Materiały dodatkowe/ arkusze diagnostyczne", "url": "https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/materialy-dodatkowe/"},
        {"name": "Przydatne", "url": "https://www.oke.poznan.pl/cms,33,egzamin_maturalny_w_formule_nbsp_2023.htm"},
        {"name": "Tutaj inne informatory", "url": "https://arkusze.pl/informator-maturalny-fizyka/"},
        

        
    ]
    
    
}
watch_later = {
     "Fizyka Co jeśli byłaby jutro": "https://www.youtube.com/watch?v=P10udMxTJ74&t=9s",
     "Matura INF": "https://www.youtube.com/watch?v=62sv9jeqz94",
     "Python na mature": "https://www.youtube.com/watch?v=gk7Sqr19W2k&list=PLpEP9TjZ__-HnaLF12Dgiq7bnNL2BqATo"
    # "Matemaks": "https://www.youtube.com/watch?v=kod_video_2",
    
    

}

OUTPUT_FILE = "index.html"

# --- SZABLONY ---
HTML_START = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matura Smooth</title>
    <link rel="stylesheet" href="style.css">
    <style>
        /* Dodatkowe style dla osadzonych plików i linków */
        embed { display: block; width: 100%; height: 400px; margin-top: 10px; border: 1px solid #ccc; }
        .links-section { margin-top: 15px; padding: 10px; background: #f0f0f0; border-radius: 5px; }
        .file-list { list-style: none; padding-left: 10px; }
        .folder-sub { margin-left: 20px; border-left: 1px solid #ddd; }
    </style>
</head>
<body>
    <header></header>
    <main>
        <nav>"""

HTML_MID = """        </nav>
        <div class="mainContent">"""

HTML_END = """        </div>
    </main>
    <aside>
        <section><h1>Calendar</h1></section>
        <section><h1>Do obejrzenia</h1>
           <ul> PROSZE_TUTAJ_LINKI </ul>
        </section>
    </aside>
    <footer></footer>
    <script>
        const navBlocks = document.querySelectorAll(".navBlock");
        const contentBlocks = document.querySelectorAll(".mainContent section");
        console.log(navBlocks);
        console.log(contentBlocks);
        for(let a=0;a<navBlocks.length;a++){

            navBlocks[a].addEventListener("click",()=>{
            contentBlocks[a].scrollIntoView();
        });
}
    </script>
      <script>
        
        let header = document.querySelector("header");
        let dates = {
            "Koniec roku": "April 24, 2026 00:00:00",
            "Matura z Polskiego": "May 5, 2026 00:00:00",
            "Matura z Matematyki": "May 6, 2026 00:00:00",
            "Matura z Angielskiego": "May 7, 2026 00:00:00",
            "Matura z Angielskiego (Rozszerzenie)": "May 8, 2026 00:00:00",
            "Matura z Fizyki": "May 15, 2026 00:00:00",
            "Matura z Informatyki": "May 18, 2026 00:00:00"
            };
        for (const key in dates) {
            
            const date = dates[key];
            const diff = timer(date);
            let dateBlock = document.createElement("div");
            dateBlock.innerHTML=key+" za <strong>"+diff+"</strong> dni";
            header.append(dateBlock);
              
        }

        function timer(date){
            const now = new Date().getTime();
            // const deadline = new Date("May 5, 2026 00:00:00").getTime();
            const deadline = new Date(date).getTime();

            const diff = deadline- now;
            var days = Math.floor(diff / (1000 * 60 * 60 * 24));
            return days;
        }

    </script>
    <script>
        const now = new Date();
        const day = new Intl.DateTimeFormat('pl-PL', { weekday: 'long' }).format(now);
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const nextDay = new Intl.DateTimeFormat('pl-PL', { weekday: 'long' }).format(tomorrow);
        const capitalizedDay = day.charAt(0).toUpperCase() + day.slice(1);
        const capitalizedNextDay = nextDay.charAt(0).toUpperCase() + nextDay.slice(1);
        let calendarBlock=document.querySelector("aside section");
        let subheader= document.createElement("h2");
        subheader.innerText= capitalizedDay;
        let subheader2= document.createElement("h2");
        subheader2.innerText= capitalizedNextDay;

        let list = document.createElement("ul");
        let nextList = document.createElement("ul");
        list.innerHTML = getList(0);
        nextList.innerHTML = getList(1);
        calendarBlock.append(subheader);
        calendarBlock.append(list);
        calendarBlock.append(subheader2);
        calendarBlock.append(nextList);

        function getList(x){
            let now ="";
            if(x==1){
                now = new Date();
                now.setDate(now.getDate() + 1);
            }else{
                now= new Date();
            }
            let content="";
            
            const day = new Intl.DateTimeFormat('pl-PL', { weekday: 'long' }).format(now);
            const capitalizedDay = day.charAt(0).toUpperCase() + day.slice(1);

            

            const calendarDays = {
                "Poniedziałek": {
                    1:"Polski/Lektura",
                    2:"Angielski/Fiszki"
                },
                "Wtorek": {
                    1:"Fizyka",
                    2:"Matma",
                    3:"Polski"
                },
                "Środa": {
                    2:"Fizyka",
                    3:"Matma",
                    4:"Polski"
                },
                "Czwartek": {
                    1:"Angielski",
                    2:"Matma",
                    3:"Fizyka"
                },
                "Piątek": {
                    1:"Fizyka",
                    2:"Matma",
                    3:"Polski",
                    4:"Angielski"
                },
                "Sobota": {
                    1:"Angielski",
                    2:"Matma"
                },
                "Niedziela": {
                    1:"Angielski",
                    2:"Matma"
                }
                };
                for (const key in calendarDays) {
                    if (key === capitalizedDay) {
                        const lessons = Object.values(calendarDays[key]); 
                        
                        for (const element of lessons) {
                            content += "<li>" + element + "</li>";
                        }
                    }
                }
                return content;
        }
        
        
    </script>
</body>
</html>"""

def get_props(folder_name):
    return folder_properties.get(folder_name, {"priority": 1000, "show": True, "id": folder_name.lower()})

def generate_file_html(file_path, base_dir):
    name = os.path.splitext(os.path.basename(file_path))[0]
    ext = os.path.splitext(file_path)[1].lower()
    rel_path = os.path.relpath(file_path, base_dir).replace("\\", "/")
    
    html_res = f'<li>📄 <a href="{html.escape(rel_path)}" target="_blank">{html.escape(name)}</a></li>'
    return html_res

def build_tree(root_dir):
    tree = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "__pycache__"]
        rel_path = os.path.relpath(dirpath, root_dir)
        
        if rel_path == ".":
            continue
            
        parts = rel_path.split(os.sep)
        current = tree
        for part in parts:
            if part not in current:
                current[part] = {"files": [], "subfolders": {}}
            if part == parts[-1]:
                current[part]["files"] = [f for f in filenames if not f.startswith(".")]
            current = current[part]["subfolders"]
    return tree

def render_content_recursive(folder_name, data, base_dir, level=2):
    parts = []
    # Pliki w tym folderze
    if data["files"]:
        parts.append('<ul class="file-list">')
        for f in sorted(data["files"]):
            if f == OUTPUT_FILE: continue
            full_p = os.path.join(base_dir, folder_name, f) # Uproszczone dla rekurencji
            # W rzeczywistości os.walk lepiej obsługuje ścieżki, tu używamy rel_path
            parts.append(generate_file_html(os.path.join(base_dir, folder_name, f), base_dir))
        parts.append('</ul>')
    
    # Podfoldery
    for sub_name, sub_data in data["subfolders"].items():
        parts.append(f'<div class="folder-sub"><h{level+1}>📁 {sub_name}</h{level+1}>')
        parts.append(render_content_recursive(os.path.join(folder_name, sub_name), sub_data, base_dir, level+1))
        parts.append('</div>')
    return "\n".join(parts)

def generate():
    links_html = "".join([f'<li><a href="{url}" target="_blank">{name}</a></li>' for name, url in watch_later.items()])
    root_dir = "."
    tree = build_tree(root_dir)
    
    # Sortowanie głównych kategorii wg priorytetu
    sorted_main_folders = sorted(
        [f for f in tree.keys() if get_props(f)["show"]],
        key=lambda x: get_props(x)["priority"]
    )

    nav_html = ""
    content_html = ""

    for folder in sorted_main_folders:
        props = get_props(folder)
        folder_id = props["id"]
        
        # Tworzenie bloków nawigacji
        nav_html += f'<div class="navBlock"><h1>{folder}</h1></div>\n'
        
        # Tworzenie sekcji treści
        content_html += f'<section id="{folder_id}">\n'
        content_html += f'<h1>{folder}</h1>\n'
        
        # Dodaj linki zewnętrzne z links.py
        links = folder_links.get(folder, [])
        if links:
            content_html += '<div class="links-section"><h3>🔗 Linki</h3><ul>'
            for l in links:
                content_html += f'<li><a href="{l["url"]}" target="_blank">{l["name"]}</a></li>'
            content_html += '</ul></div>'

        # Dodaj pliki i podfoldery
        content_html += render_content_recursive(folder, tree[folder], root_dir)
        content_html += '</section>\n'

    # Zapis do pliku
    final_html = (HTML_START + nav_html + HTML_MID + content_html + HTML_END).replace("PROSZE_TUTAJ_LINKI", links_html)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"✔️ Wygenerowano {OUTPUT_FILE}")

if __name__ == "__main__":
    generate()